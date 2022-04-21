from venv import psycopg2 as ps
import os
from create_bot import bot

def psy_start():
    global base, cur
    base = ps.connect(os.environ.get('DATABASE_URL'), sslmode='require')
    cur = base.cursor()
    if base:
        print('База данных успешно открыта')
    base.execute('CREATE TABLE IF NOT EXISTS test(img TEXT, name TEXT PRIMARY KEY, description TEXT, price BLOB)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES(?, ?, ?, ?)', tuple(data.values()))
        base.commit()
        print('Данные добавлены в базу данных')

async def sql_read(message):
    for ret in cur.execute("SELECT * FROM test").fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОпис: {ret[2]}\nПосилання: {ret[-1]}')

async def sql_read2():
    return cur.execute("SELECT * FROM test").fetchall()

async def sql_delete_command(data):
    cur.execute('DELETE FROM test WHERE name = ?', (data,))
    base.commit()
