from aiogram import types
import random
from config import bot, Dispatcher


async def game(message: types.Message):
    if message.from_user.id:
        games = ['🎲', '🏏', '⚽']
        if message.text.startswith('game'):
            await bot.send_message(message.chat.id, random.choice(games))
        if message.text.startswith('!pin'):
            await bot.pin_chat_message(message.chat.id, message.message_id)
        await bot.send_message(message.from_user.id, message.text)


def register_game_handler(dp: Dispatcher):
    dp.register_message_handler(game)