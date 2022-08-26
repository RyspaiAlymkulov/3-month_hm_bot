import random
import sqlite3
from config import bot


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключена!")

    db.execute("CREATE TABLE IF NOT EXISTS fsmAdminMenu "
               "(photo TEXT, name TEXT, "
               "description TEXT, price INTEGER)")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO fsmAdminMenu VALUES "
                       "(?, ?, ?, ?)",
                       tuple(data.values()))
        db.commit()


async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM fsmAdminMenu").fetchall()
    random_menu = random.choice(result)
    await bot.send_photo(message.from_user.id,
                         random_menu[0],
                         caption=f"Блюдо: {random_menu[1]}\n"
                                 f"Описание: {random_menu[2]}\n"
                                 f"Цена: {random_menu[3]}\n")


async def sql_command_all():
    return cursor.execute("SELECT * FROM fsmAdminMenu").fetchall()


async def sql_command_delete(name):
    cursor.execute("DELETE FROM fsmAdminMenu WHERE name == ?", (name,))
    db.commit()


async def sql_command_get_all_name():
    return cursor.execute("SELECT name FROM fsmAdminMenu").fetchall()






