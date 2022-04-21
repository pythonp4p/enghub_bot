from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Клавиатура для администратора
button_load = KeyboardButton('/Загрузить')
button_delete = KeyboardButton('/Удалить')
button_choose = KeyboardButton('/Выбрать')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button_case_admin.add(button_load, button_delete).add(button_choose)
