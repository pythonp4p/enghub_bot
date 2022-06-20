from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from keyboards.client_inline_kb import urlkb, proginkb, selfkb
from aiogram.types import ReplyKeyboardRemove
import time

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text


# !                                      КЛИЕНТСКАЯ ЧАСТЬ                                                       #
# При помощи диспечера записываем декоратор. Сюда будет попадать вот такой декоратор.
# Он обозначает событие, когда в наш чат кто то что то пишет вообще
# * В commands= перечисляем команды на которые будет реагировать наш бот при помощи этого handlerа
# * Тоесть этот handler сработает тогда, когда пользователь напишет /start или /help
# * И также этот же самый handler сработает тогда, когда пользователь добавиться к нашему боту
# ? В телеграмме бот не может написать пользователю первый, тоесть если пользователь не написал боту
# ? или не зашел в группу. А наш код далее будет писать ему в личку, поэтому прописываем обработчик ошибок
# ^ Записываем код, который сработает во время команды /start и /help
# ^ В данном случае, мы будем отправлять пользователю сообщение в личку
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



# & Тут нам в функции нужно записать команды для регистрации handlerов для нашего бота и передать уже
# & при помощи этой функции все эти handlerы в основной файл
# & Сюда в эту функцию необходимо передать диспечер и написать для него аннотацию типа
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_place_command,
                                commands=['Learning_materials'])
    dp.register_message_handler(call_me_command, commands=['Contacts'])
    dp.register_message_handler(max_tests_command, commands=['Syllabus'])
    dp.register_message_handler(self_study_command, commands=['Self_study'])
