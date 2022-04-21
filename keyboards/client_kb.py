from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

# & Для того чтобы создать каждую кнопку по отдельности, нам необходим класс KeyboardButton
# & Сюда мы с вами записываем строку, тоесть то что будет отображаться на кнопке и эту же самую строку
# & эта кнопка отправляет нашему боту
# & Мы создаем кнопку и указываем ту команду которая будет на кнопке и которая будет отправляться
# & нашему боту для выполнения и все это сохраняем в переменную

# ^ Далее, мы создаем еще одну переменную и здесь запускаем класс ReplyKeyboardMarkup.
# ^ Этот класс замещает клавиатуру ОБЫЧНУЮ НА ТУ КОТОРУЮ МЫ СОЗДАЕМ

# ^ И в нем, как дополнительный аргумент, указываем чтобы наши кнопки меняли свой размер
# ^ в зависимости от размера текста на каждой кнопке. resize_keyboard=True

# ^ И чтобы дать такую возможность как спрятать клавиатуру после того как пользователь сделал какой то выбор,
# ^ нужно еще одним дополнительным аргументом указать one_time_keyboard=True

# ^ Ну а чтобы УДАЛИТЬ клавиатуру после того как пользователь сделал какой то выбор,
# ^ нужно удалить запись one_time_keyboard=True а в функцию которая отправляет сообщение(другой файл:client.py)
# ^ записать reply_markup=ReplyKeyboardRemove() дополнительным аргументом после сообщения которое будет
# ^ отпралено пльзователю после нажатия на кнопку

# * И после, уже к замещенной клавиатуре, мы методом .add добавляем наши кнопки
# * Соответственно, этот метод каждый раз добавляет кнопку с новой строки
# ! Метод .insert. От .add он отличаеться тем, что добавляет кнопку не с новой строки,
# ! а добавляет если есть где то в строке место

# ? Добавляем одни кнопки в строку а другие с новой строки и сохраняем в переменную
# ! Метод row() это добавление всех кнопок в строку

# ~ Есть две кнопки исключения, которые отправляют не то что в них написано
# ~ Это кнопки для того чтобы поделиться контактом, своим номером телефона и своим рассположением


# &
b2 = KeyboardButton('/Learning_materials')
b4 = KeyboardButton('/Contacts')
b8 = KeyboardButton('/Syllabus')
b5 = KeyboardButton('/Tests')
b10 = KeyboardButton('/Self_study')

# ^
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

# ?
# !
kb_client.add(b8, b2,).add(b5).row(b4, b10)
