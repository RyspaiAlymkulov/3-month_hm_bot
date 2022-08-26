import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot


async def get_menu_name():  #message: types.Message
    # global chat_id
    ADMIN_ID = 1383352235
    # chat_id = message.from_user.id
    await bot.send_message(chat_id=ADMIN_ID, text="Добрый день, сегодня вам нужно заполнить меню")


# async def go_to_sleep():
#     await bot.send_message(chat_id=chat_id, text="иди спать")
#
#
# async def wake_up():
#     await bot.send_message(chat_id=chat_id, caption="Доброе утро")


async def scheduler():
    aioschedule.every().friday.at("13:30").do(get_menu_name)
    # aioschedule.every().friday.at("13:06").do(wake_up)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(3)


def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_menu_name,
                                lambda word: "напомни" in word.text)




