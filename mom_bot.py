from email import message
import os
from venv import psycopg2
from aiogram.utils import executor
from create_bot import dp, bot, URL_APP, DB_URI

# Запускаем функцию старта базы данных
async def on_startup(dp):
    await bot.set_webhook(url=URL_APP)

async def on_shutdown(dp):
    await bot.delete_webhook()

db_connection = psycopg2.connect(DB_URI, sslmode="require")
db_object = db_connection.cursor()


# Импортируем функции из наших файлов
from handlers import client, other
# Запускаем наши функции
id = message.from_user.id
username = message.from_user.username
client.register_handlers_client(dp)
db_object.execute(f"SELECT id FROM users WHERE id = {id}")
result = db_object.fetchone()
if not result:
    db_object.execute("INSERT INTO users(id, username, messages) VALUES (%s, %s, %s)", (id, username, 0))
    db_connection.commit()
#admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


executor.start_webhook(
    dispatcher=dp,
    webhook_path='',
    on_startup=on_startup,
    on_shutdown=on_shutdown,
    skip_updates=True,
    host="0.0.0.0",
    port=int(os.environ.get('PORT', 5000)),
)
