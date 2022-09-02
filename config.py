from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = config("TOKEN")
print(TOKEN)
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
ADMIN = 1383352235
URL = "https://pythongeek2000.herokuapp.com/"