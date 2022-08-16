from aiogram.utils import executor
from config import dp, bot
from handlers import client, extra, callback, admin, echo


client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
extra.register_game_handler(dp)
echo.register_echo_message(dp)


# @dp.message_handler()
# async def echo(message: types.Message):
#     try:
#         message.text.isdigit
#         message.text = int(message.text)
#         message.text *= int(2)
#         await bot.send_message(message.from_user.id, message.text)
#     except:
#         await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
