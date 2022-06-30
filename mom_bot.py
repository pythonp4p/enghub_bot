
import os

from aiogram.utils import executor
from create_bot import dp, bot, URL_APP


async def on_startup(dp):
    await bot.set_webhook(url=URL_APP)

async def on_shutdown(dp):
    await bot.delete_webhook()


from handlers import client, other

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
