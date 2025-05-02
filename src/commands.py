from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from src.database import async_session
from src.models import CaseModel

router = Router()

@router.message(Command(commands="start"))
async def start(message: Message):
    await message.answer("Привет! Что хочешь записать?")


@router.message(Command(commands="cancel"))
async def cancel(message: Message):
    await message.answer("Функция в разработке...")


@router.message()
async def save_case(message: Message):
    msg = message.text.split("#")
    try:
        async with async_session() as session:
            new_case = CaseModel(tag=msg[0], case=msg[1].strip())
            session.add(new_case)
            await session.commit()
        await message.answer("""Готово! Заметка добавлена в базу данных.
        Для отмены нажмите /cancel""")
    except:
        await message.answer("Ошибка! Заметка должна быть в формате:\n tag#\n text")