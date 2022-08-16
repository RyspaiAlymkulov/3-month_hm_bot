from aiogram import Bot, Dispatcher
from decouple import config

TOKEN = config("TOKEN")
print(TOKEN)
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
ADMIN = [1383352235, ]
