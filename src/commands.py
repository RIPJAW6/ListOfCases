from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from src.database import async_session
from src.models import CaseModel

router = Router()

@router.message(Command(commands="start"))
async def start(message: Message):
    await message.answer("Привет! Что хочешь записать?")


@router.message()
async def save_case(message: Message):
    async with async_session() as session:
        new_case = CaseModel(case=message.text)
        session.add(new_case)
        await session.commit()
    await message.answer("Готово! Запись сделана.")

