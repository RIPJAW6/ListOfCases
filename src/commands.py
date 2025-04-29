from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command(commands="start"))
async def start(message: Message):
    await message.answer("""
    Привет! Отправь мне какую-либо запись, 
    которую ты хочешь сохранить, а я добавлю её в БД.""")
