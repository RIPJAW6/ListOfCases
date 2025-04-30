from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from src.models import CaseModel
from src.database import session

router = Router()

@router.message(Command(commands="start"))
async def start(message: Message):
    await message.answer("Привет! Что хочешь записать?")


@router.message()
async def save_case(message: Message):
    new_case = CaseModel(case=message.text)
    session.add(new_case)
    session.commit()
    await message.answer("Готово! Запись сделана.")

