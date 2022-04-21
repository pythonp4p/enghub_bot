
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from base import base_1, base_2, base_3
from keyboards import admin_kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# FSMContext нужен для аннотации типа. Тоесть мы будем указывать в handlerах о том что этот handler
# используеться конкретно в машине состояний

ID = None

# ! Для начала нам необходимо создать классы наших состояний
# * Нам здесь необходимо наследоваться от базового класса StatesGroup
# * В данном случае у нас будет 4 состояния. Тоесть у нас будет класс с 4 пунктами последовательных вопросов.
# ~ 1. Отправка фотографий
# ~ 2. Обозначение названия пиццы
# ~ 3. Добавление описания
# ~ 4. Выставление цены на пиццу
# * Сначала заводим экземпляр и здесь мы запускаем класс State. Это необходимо для того, чтобы обозначить
# * что это будет конкректно состояние бота и мы потом будем переходить между ними
# * Далее также заводим экземпляр и запускаем класс State
# * Далее заводим экземпляр с описанием нашей пиццы и запускаем класс State
# * И тоже самое проделываем с ценой
# ^ Этот класс необходим для того чтобы бот переходил между этими состояниями
# ^ которые мы пропишем, этот переход. В handlerах

# ? После пишем базовый handler который запускает нашу машину состояний
# ? В нем необходимо указать команду запуска класса FSMAdmin.method.set(). Тоеcть запустить метод
# ? Тоесть, как только админ пишет Загрузить, срабатывает этот handler. И мы здесь становимся ботом
# ? в состоянии загрузки, тоесть он теперь будет ожидать конкретного ответа от пользователя, тоесть бот
# ? перейдет из обычного режима работы в режим работы машины состояний именно благодаря тому что мы там
# ? устанавливаем переход для бота перейти в этот режим.

# & Соответсвенно теперь нам необходимо записать handler который поймает ответ от пользователя

# & В content_types указываем photo, так как мы будем отправлять картинку нашей пиццы,
# & и в параметр state записываем =FSMAdmin.photo, так как мы ранее при помощи await FSMAdmin.photo.set()
# & поставили нашего бота в состояние ожидания ответа на первый вопрос.

# & Так как мы передаем =FSMAdmin.photo, именнно в этот handler попадет первый ответ от админа

# & Далее записываем ассинхронную функцию, в нее указываем параметр с аннотицией типа. message : types.Message
# & и также указываем еще один параметр с аннотацией типа. state: FSMContext

# & Далее так как этот handler сработает на отправку фото, нам необходимо теперь сохранить полученый результат
# & в словарь машины состояний
# & Для этого открываем словарь в который мы записываем значение по ключу ['photo'] мы пишем сюда.

# ! В телеграм каждому отправленому фото присваиваеться свой уникальный id номер, который мы запишем
# ! в базу данных, и бот отправляя пользователю картинку, будет отправлять эту картинку по id.

# & Соответсвенно, мы здесь из message.photo по индексу 0 получаем id этого изображения
# & и пишем в словарь машины состояний

# & Далее так как на первый вопрос пользователь уже ответил, мы здесь через оператор await обращаемся
# & к FSMAdmin и используем метод .next(). Тоесть переводим нашего бота в ожидание слeдущего ответа.
# & И после пишем ему сообщение "Теперь введи название"

# ~ И теперь дальше мы пишем handler для того чтобы поймать следующий ответ пользователя на вот этот
# ~ поставленный вопрос "Теперь введи название"

# ~ В нем мы также пишем state=FSMAdmin.name, указывая что в этот handler будет попадать второй ответ

# ~ Также записываем аннотации типа к message и state

# ~ Опять открываем словарь хранения информации как data

# ~ И здесь по ключу ['name'] вытягиваем из события СООБЩЕНИЕ текст, тоесть название для нашей пиццы

# ~ Далее при помощи await FSMAdmin.next() опять переходим в следущее состояние, в котором администратор
# ~ будет вводить описание этой пиццы

# ~ Ну и соответственно пишем ему введи описание для пиццы

# todo. В последнем handler делаем тоже самое. НО брать мы будем число, поэтому записываем
# todo data['price'] = float(message.text)

# todo. Ну и чтобы завершить состояние, нам необходимо записать await state.finish().

#todoКак только записана эта команда, ТО БОТ ВЫХОДИТ ИЗ МАШИНЫ СОСТОЯНИЯ И ПОЛНОСТЬЮ ОЧИЩАЕТ ВСЕ ЧТО МЫ ЗАПИСАЛИ.
# todo ПОЭТОМУ, все то что мы хотим сделать с получеными данными, необходимо сделать ДО ЭТОЙ КОМАНДЫ

#todo Чтобы это сделать есть 2 варианта   1. Записать в базу данных(сделаем потом)
#todo                                     2. Вывести на экран готовую публикацию(сделаем сейчас)

# ! handler Для выхода из состояний
# В первом декораторе указываеться state="*" тоесть в каком бы из 4 состояний бот не находился
# и команда отмена. * означает любое состояние машины состояний

# Во втором декораторе у нас фильтр текста, тоесть тут мы записываем какой конкретно текст ("отмена")
# и любое состояние машины состояний

# Потом анотации типа

# Далее мы проверяем в каком состоянии сейчас находиться бот.
# И проверяем. Если состояния никакого, тоесть сейчас не работает машина состояний, то что введеться,
# в данном случае "отмена". НЕ ВЫПОЛНИТЬСЯ.

# Если же бот находиться в каком либо из состояний, сработывает следующая строка await state.finish(),
# тоесть мы просто закрываем эту машину состояний. И выводим сообщение ок

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()
    choose = State()

# Получаем id текущего модератора
# ! Тоесть даем доступ к админке только администратору группы где состоит бот.
# Как только пользователь вводит комманду 'moderator' ОН ДОЛЖЕН ЭТО ДЕЛАТЬ В ГРУППЕ,
# и если он являеться им, мы объявляем переменную ID глобальной и присваиваем в нее айди этого модератора.
# Далее пишем ему в личку и удаляем сообщение из групового чата
#@dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что надо хозяин?', reply_markup=admin_kb.button_case_admin)
    await message.delete()

#?
#? Начало диалога загрузки нового пункта меню
#@dp.message_handler(commands='Загрузить', state=None)
async def cm_start(message : types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply('Загрузи фото')

# ! Выход из состояний
#@dp.message_handler(state="*", commands='отмена')
#@dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('OK')

#&
#& Ловим первый ответ и пишем его в словарь
#@dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply("Теперь введи название")

# ~
# ~Ловим второй ответ
#@dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply("Введи описание")

#
# Ловим третий ответ
#@dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.reply("Введи ссылку")

#todo
#todo. Ловим последний ответ и используем полученные данные
#@dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = message.text
        await FSMAdmin.next()
        await message.reply("Виберіть куди завантажити цей матеріал")
        #await sqlite_db.sql_add_command(state)
        #await state.finish()

choosekb = InlineKeyboardMarkup(row_width=1)
choosekb.add(InlineKeyboardButton(text='3 курс', callback_data='but_3 курс')).add(InlineKeyboardButton(text='4 курс', callback_data='but_4 курс')).add(InlineKeyboardButton(text='Завантажити для self_study', callback_data='but_5 курс'))


@dp.message_handler(commands=['Выбрать'], state=FSMAdmin.choose)
async def pizza_menu_command(message: types.Message):
    await message.answer("Завантажити в:", reply_markup=choosekb)

@dp.callback_query_handler(Text(startswith='but_'), state=FSMAdmin.choose)
async def buttonrrr_call(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'but_3 курс':
        await callback.message.edit_text("Выбран 3 курс")
        await base_1.sql_add_command(state)
        await state.finish()
    if callback.data == 'but_4 курс':
        await callback.message.edit_text("Выбран 4 курс")
        await base_2.sql_add_command(state)
        await state.finish()
    if callback.data == 'but_5 курс':
        await callback.message.edit_text("Загружено для self_study")
        await base_3.sql_add_command(state)
        await state.finish()

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
    await base_1.sql_delete_command(callback_query.data.replace('del ', ''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удалено', show_alert=True)

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('dep '))
async def del_callback_run1(callback_query: types.CallbackQuery):
    await base_2.sql_delete_commandd(callback_query.data.replace('dep ', ''))
    await callback_query.answer(text=f'{callback_query.data.replace("dep ", "")} удалено', show_alert=True)

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('det '))
async def del_callback_run(callback_query: types.CallbackQuery):
    await base_3.sql_delete_commanddd(callback_query.data.replace('det ', ''))
    await callback_query.answer(text=f'{callback_query.data.replace("det ", "")} удалено', show_alert=True)

#@dp.message_handler(commands=['Удалить'])
async def delete_item(message: types.Message):
    if message.from_user.id == ID:
            read = await base_1.sql_read2()
            read1 = await base_2.sql_read2()
            read2 = await base_3.sql_read2()
            for ret in read:
                await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОпис: {ret[2]}\nСсылка: {ret[-1]}')
                await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
                    add(InlineKeyboardButton(f'Удалить,{ret[1]}', callback_data=f'del {ret[1]}')))
            for ret1 in read1:
                        await bot.send_photo(message.from_user.id, ret1[0], f'{ret1[1]}\nОпис: {ret1[2]}\nСсылка: {ret1[-1]}')
                        await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
                            add(InlineKeyboardButton(f'Удалить,{ret1[1]}', callback_data=f'dep {ret1[1]}')))
            for ret2 in read2:
                    await bot.send_photo(message.from_user.id, ret2[0], f'{ret2[1]}\nОпис: {ret2[2]}\nСсылка: {ret2[-1]}')
                    await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
                        add(InlineKeyboardButton(f'Удалить,{ret2[1]}', callback_data=f'det {ret2[1]}')))


# ! Регестрируем handlerы
def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*" )
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(delete_item, commands=['Удалить'])
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)
