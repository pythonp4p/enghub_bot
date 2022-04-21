from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Запускаем класс MemoryStorage и сохраняем в переменную. И там где у нас запуск класса Dispatcher в который мы
# передаем класс бота, дописываем storage=storage. Тоесть в параметр передаем наш экземпляр MemoryStorage
storage=MemoryStorage()

TOKEN = '5343498342:AAFqLRlZTSbnrTJXoShx5JBCmcJ8hKwCq0o'
URL_APP = 'https://enghub.herokuapp.com/'
# Инициализируем нашего бота, читаем токен
bot = Bot(token=TOKEN)
# Инициализируем Dispatcher и передаем сюда экземпляр нашего бота
dp = Dispatcher(bot, storage=storage)
