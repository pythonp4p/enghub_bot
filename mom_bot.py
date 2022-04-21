import os
from venv import psycopg2 as ps
from aiogram.utils import executor
from create_bot import dp, bot, URL_APP
from base import base_1, base_2, base_3

base = ps.connect(os.environ.get('DATABASE_URL'), sslmode='require')
cur = base.cursor()

# Запускаем функцию старта базы данных
async def on_startup(dp):
    await bot.set_webhook(url=URL_APP)

async def on_shutdown(dp):
    await bot.delete_webhook()
    cur.close()
    base_1.close()




# Импортируем функции из наших файлов
from handlers import client, other
# Запускаем наши функции
client.register_handlers_client(dp)
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
