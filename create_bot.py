from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Запускаем класс MemoryStorage и сохраняем в переменную. И там где у нас запуск класса Dispatcher в который мы
# передаем класс бота, дописываем storage=storage. Тоесть в параметр передаем наш экземпляр MemoryStorage
storage=MemoryStorage()

TOKEN = '5343498342:AAFqLRlZTSbnrTJXoShx5JBCmcJ8hKwCq0o'
URL_APP = 'https://enghub.herokuapp.com/'
DB_URI = 'postgres://zuxviwjkwqgwgb:5e0d5a7f5b8f2af450186cb74364aa08522fe820ac8520d03ddbb10faa6c6950@ec2-52-49-120-150.eu-west-1.compute.amazonaws.com:5432/d5b2plf6pn83k3'
# Инициализируем нашего бота, читаем токен
bot = Bot(token=TOKEN)
# Инициализируем Dispatcher и передаем сюда экземпляр нашего бота
dp = Dispatcher(bot, storage=storage)
