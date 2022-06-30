from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from keyboards.client_inline_kb import urlkb, proginkb, selfkb
from aiogram.types import ReplyKeyboardRemove
import time

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text

#@dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):
    try:
        await bot.send_message(
            message.from_user.id,
            'Шановні відвідувачі, цей бот створено для допомоги студентам в опануванні англійської мови на рівні В2+ та в оволодінні вміннями ділового англомовного листування.',
            reply_markup=kb_client)
        time.sleep(5)
        await bot.send_message(message.from_user.id, 'Гарного дня)')
        await message.delete()
    except:
        await message.reply(
            'Общение с ботом челез лс, напишите ему:\nhttp://t.me/eng_hub_bot'
        )
        


#@dp.message_handler(commands=['Learning_materials'])
async def pizza_place_command(message: types.Message):
    await message.answer('Ваші навчальні матеріали', reply_markup=proginkb)


#@dp.message_handler(commands=['Syllabus'])
async def max_tests_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Ваша навчальна програма', reply_markup=urlkb)

#@dp.message_handler(commands=['Self_study'])
async def self_study_command(message: types.Message):
    await message.answer('Матеріали для самостійного проходження', reply_markup=selfkb)


async def call_me_command(message: types.Message):
    await bot.send_message(message.from_user.id,'Мій телеграм аккаунт:\n https://t.me/Tania_Pasechnik')

inkb = InlineKeyboardMarkup(row_width=1)
inkb.add(InlineKeyboardButton(text='3 курс', url='https://docs.google.com/forms/d/1OuGrAnPUGP3li7gNwzVj8pJWCvj0c3Gzd84JDgXRigk/viewform?edit_requested=true')).add(InlineKeyboardButton(text='4 курс', url='https://learnenglish.britishcouncil.org/grammar/b1-b2-grammar'))


@dp.message_handler(commands=['Tests'])
async def pizza_menu_command(message: types.Message):
    await message.answer("Оберіть свій курс", reply_markup=inkb)

    
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_place_command,
                                commands=['Learning_materials'])
    dp.register_message_handler(call_me_command, commands=['Contacts'])
    dp.register_message_handler(max_tests_command, commands=['Syllabus'])
    dp.register_message_handler(self_study_command, commands=['Self_study'])
