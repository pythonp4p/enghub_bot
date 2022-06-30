from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage=MemoryStorage()

TOKEN = '55555'
URL_APP = 'https://enghub.herokuapp.com/'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
