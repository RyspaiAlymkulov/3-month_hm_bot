from aiogram import types
from config import bot, Dispatcher


async def echo(message: types.Message):
    try:
        message.text.isdigit
        message.text = int(message.text)
        message.text *= 2
        await bot.send_message(message.from_user.id, message.text)
    except:
        await bot.send_message(message.from_user.id, message.text)


def register_echo_message(dp: Dispatcher):
    dp.register_message_handler(echo)