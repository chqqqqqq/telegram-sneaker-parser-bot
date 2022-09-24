import asyncio
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from app.handlers.common import register_handlers_common
from app.handlers.brands import register_handlers_brands
from config import token


async def main():

    bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
    dp = Dispatcher(bot, storage=MemoryStorage())

    register_handlers_common(dp)
    register_handlers_brands(dp)

    await dp.start_polling()


if __name__ == '__main__':

    asyncio.run(main())