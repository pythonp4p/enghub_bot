from aiogram.utils import executor
from create_bot import dp
#from data_base import sqlite_db, sqlite_db_2, sqlite_db_3

# Запускаем функцию старта базы данных
async def on_startup(_):
    print('Бот вышел в онлайн')
    #sqlite_db.sql_start()
    #sqlite_db_2.sql_start()
    #sqlite_db_3.sql_start()

# Импортируем функции из наших файлов
from handlers import client, other
# Запускаем наши функции
client.register_handlers_client(dp)
#admin.register_handlers_admin(dp)
other.register_handlers_other(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
