from config import URL, bot
from decouple import config
import asyncio
import logging
from aiogram.utils import executor
from config import dp
from handlers import client, extra, callback, admin, echo, fsmAdminMenu, notification, inline
from database import bot_db


async def on_startup(_):
    await bot.set_webhook(URL)
    asyncio.create_task(notification.scheduler())
    bot_db.sql_create()


async def on_shutdown(dp):
    await bot.delete_webhook()


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
callback.register_handlers_callback(dp)
fsmAdminMenu.register_handlers_fsm_menu(dp)
extra.register_game_handler(dp)
notification.register_handlers_notification(dp)
inline.register_handlers_inline(dp)

echo.register_echo_message(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_webhook(
        dispatcher=dp,
        webhook_path="",
        on_shutdown=on_shutdown,
        on_startup=on_startup,
        skip_updates=True,
        host='0.0.0.0',
        port=config("PORT", cast=int)
    )
