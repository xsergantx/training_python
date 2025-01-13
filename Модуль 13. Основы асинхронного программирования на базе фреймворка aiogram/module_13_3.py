"""
Задача "Он мне ответил!":
Измените функции start и all_messages так, чтобы вместо вывода в консоль строки отправлялись
в чате телеграм.
Запустите ваш Telegram-бот и проверьте его на работоспособность.
"""


from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())


@dp.message_handler(text = ["Привет"])
async def all_message(message):
    await message.answer("Введите команду /start, чтобы начать общение.")# то ответ будет такой в ТГ

@dp.message_handler(text = ["/start"])
async def all_message(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
