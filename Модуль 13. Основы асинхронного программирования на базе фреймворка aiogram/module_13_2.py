"""
Задача "Бот поддержки (Начало)":
К коду из подготовительного видео напишите две асинхронные функции:
start(message) - печатает строку в консоли 'Привет! Я бот помогающий твоему здоровью.' .
Запускается только когда написана команда '/start' в чате с ботом. (используйте соответствующий
декоратор)
all_massages(message) - печатает строку в консоли 'Введите команду /start, чтобы начать общение.'.
 Запускается при любом обращении не описанном ранее. (используйте соответствующий декоратор)
"""


from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7582957828:AAG7NpEHnKHB8-QQj1mV7L7XwtAfCTXmTsc"
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())


@dp.message_handler(text = ["/start"])
async def all_message(message):
    print("Привет! Я бот помогающий твоему здоровью")

@dp.message_handler()#проверка на получение сообщения из бота
async def all_message(message):
    print("Введите команду /start, чтобы начать общение.")




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
