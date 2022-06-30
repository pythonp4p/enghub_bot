from aiogram import types, Dispatcher
from create_bot import dp
import json, string

#@dp.message_handler()
async def stop_mats(message : types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('bad_words.json')))) != set():
            await message.reply('Маты запрещены')
            await message.delete()

def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(stop_mats)
