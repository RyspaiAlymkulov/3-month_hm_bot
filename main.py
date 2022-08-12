from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ContentType, Message, InputFile
from aiogram.utils import executor
from config import dp, bot


@dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"hello{message.from_user.full_name}")


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Следующий вопрос",
                                         callback_data="button_call_1")
    markup.add(button_call_1)
    question = "Какой персонаж мультика живет в ананасе под водой?"
    answers = [
        'Рик и Морти',
        'Немор',
        'Аквамен',
        'Губка боб'
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="нельзя не знать",
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
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


@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_file_id(message: Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(text='/mem')
async def send_photo(message: Message):
    chat_id = message.from_user.id

    # photo_file_id = 'sdasd'
    # photo_url = 'sf'
    photo_bytes1 = InputFile(path_or_bytesio='media/proga.jpeg')
    photo_bytes2 = InputFile(path_or_bytesio='media/proga2.jpg')
    photo_bytes3 = InputFile(path_or_bytesio='media/proga3.jpg')

    await dp.bot.send_photo(chat_id=chat_id, photo=photo_bytes1)
    await dp.bot.send_photo(chat_id=chat_id, photo=photo_bytes2)
    await dp.bot.send_photo(chat_id=chat_id, photo=photo_bytes3)


# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     await bot.send_message(msg.from_user.id, msg.text)


@dp.message_handler()
async def echo(message: types.Message):
    try:
        message.text.isdigit
        message.text = int(message.text)
        message.text *= int(2)
        await bot.send_message(message.from_user.id, message.text)
    except:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
