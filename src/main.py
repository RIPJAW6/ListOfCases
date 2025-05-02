import os
from dotenv import load_dotenv
import asyncio
from aiogram import Bot, Dispatcher
from src.commands import router

dp = Dispatcher()
dp.include_router(router)

async def main():

    # Путь "dotenv_path=" в load_dotenv() указывается опционально

    load_dotenv()
    bot = Bot(token=os.getenv("TOKEN"))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())