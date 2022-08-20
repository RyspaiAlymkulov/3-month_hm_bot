import logging

from aiogram.utils import executor
from config import dp, bot
from handlers import client, extra, callback, admin, echo, fsmAdminMenu
from database import bot_db


async def on_startup(_):
    bot_db.sql_create()


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
callback.register_handlers_callback(dp)
fsmAdminMenu.register_handlers_fsm_menu(dp)
extra.register_game_handler(dp)


echo.register_echo_message(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
