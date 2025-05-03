from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from sqlalchemy import delete, select
from src.database import async_session
from src.models import CaseModel

router = Router()
ram = []

@router.message(Command(commands="start"))
async def start(message: Message):
    await message.answer("""Привет! Что хочешь записать в базу данных?
Я принимаю записи в формате: тег# текст
Для поиска всех заметок по тегу, введи запрос в формате: тег$""")


@router.message(Command(commands="cancel"))
async def cancel(message: Message):
    try:
        async with async_session() as session:
            msg = delete(CaseModel).filter_by(tag=ram[0], case=ram[1])
            await session.execute(msg)
            await session.commit()
        await message.answer("Добавление последней заметки отменено.")
        ram.clear()
    except:
        await message.answer("Добавление последней заметки уже было отменено.")


async def search(msg) -> list:
    search_query = msg.split("$")[0].strip().lower()
    async with async_session() as session:
        request = select(CaseModel).filter_by(tag=search_query)
        results = await session.execute(request)
        return list(results.scalars())


async def insert(msg):
    ram.clear()
    request_to_add = msg.split("#")
    async with async_session() as session:
        new_case = CaseModel(tag=request_to_add[0].strip().lower(), case=request_to_add[1].strip())
        session.add(new_case)
        await session.commit()
        ram.append(request_to_add[0])
        ram.append(request_to_add[1].strip())
    return """Готово! Заметка добавлена в базу данных.
Для отмены нажмите /cancel"""


@router.message()
async def msg_processing(message: Message):
    msg = message.text
    if "$" in msg:
        results = await search(msg)
        if len(results) == 0:
            await message.answer("По указанному тегу ничего не найдено.")
        else:
            for result in results:
                await message.answer(f"{result}")
    elif "#" in msg:
        result_2 = await insert(msg)
        await message.answer(result_2)
    else:
        await message.answer("Ошибка! Заметка должна быть в формате: тег# текст")