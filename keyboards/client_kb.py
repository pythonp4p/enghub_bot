from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

b2 = KeyboardButton('/Learning_materials')
b4 = KeyboardButton('/Contacts')
b8 = KeyboardButton('/Syllabus')
b5 = KeyboardButton('/Tests')
b10 = KeyboardButton('/Self_study')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)


kb_client.add(b8, b2,).add(b5).row(b4, b10)
