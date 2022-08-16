from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_2)

    question = "Какая страна производит больше всего кофе в мире?"
    answers = [
        'Колумбия',
        'Бразилия',
        'Индонезия',
        'Вьетнам'
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Эта страна была пятикратным чемпионом мира по футболу. 1958, 1962, 1970, 1994, 2002"
    )


async def quiz_3(call: types.CallbackQuery):
    question = "Какой безалкогольный напиток был взят в космос?"
    answers = [
        'Пепси',
        'Фанта',
        'Кока кола',
        'Снапл'
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2,
                                       lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3,
                                       lambda call: call.data == "button_call_2")