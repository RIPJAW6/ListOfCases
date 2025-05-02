from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from sqlalchemy import delete
from src.database import async_session
from src.models import CaseModel

router = Router()
ram = []

@router.message(Command(commands="start"))
async def start(message: Message):
    await message.answer("""Привет! Что хочешь записать в базу данных?
Я принимаю записи в формате:\ntag#\ntext""")


@router.message(Command(commands="cancel"))
async def cancel(message: Message):
    try:
        async with async_session() as session:
            msg = delete(CaseModel).filter_by(tag=ram[0], case=ram[1])
            await session.execute(msg)
            await session.commit()
        await message.answer("Добавление заметки отменено.")
        ram.clear()
    except:
        await message.answer("Добавление заметки уже было отменено.")


@router.message(Command(commands="search"))
async def search(message: Message):
    await message.answer("""Для поиска всех заметок по тегу, введите запрос в формате:
tag$""")


@router.message()
async def save(message: Message):
    ram.clear()
    msg = message.text.split("#")
    try:
        async with async_session() as session:
            new_case = CaseModel(tag=msg[0], case=msg[1].strip())
            session.add(new_case)
            await session.commit()
        await message.answer("""Готово! Заметка добавлена в базу данных.
        Для отмены нажмите /cancel""")
        ram.append(msg[0])
        ram.append(msg[1].strip())
    except:
        await message.answer("Ошибка! Заметка должна быть в формате:\ntag#\ntext")