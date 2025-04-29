import os
from dotenv import load_dotenv
import asyncio
from aiogram import Bot, Dispatcher
from src.commands import router

dp = Dispatcher()
dp.include_router(router)

async def main():

    # Путь в load_dotenv указывается опционально, можно и просто load_dotenv()

    load_dotenv(dotenv_path="C:\\Users\\Александр\\PycharmProjects\\ListOfCases\\.env")
    bot = Bot(token=os.getenv("TOKEN"))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())