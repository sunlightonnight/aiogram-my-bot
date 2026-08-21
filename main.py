from os import getenv
from dotenv import load_dotenv
import asyncio
from aiogram import Bot, Dispatcher
from handlers import router 

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()
dp.include_router(router)

async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)
    print("Bot is running...")

if __name__ == "__main__":
    asyncio.run(main())