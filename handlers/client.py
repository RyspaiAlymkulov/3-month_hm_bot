from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ContentType, Message, InputFile
from config import bot, dp


async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Привет {message.from_user.full_name}\n"
                           f"1. Я могу фильтровать твои сообщения, так что будь осторожен\n"
                           f"Не матерись {message.from_user.full_name}\n"
                           f"2. Так же могу на /quiz вывести тебе викторину или опросник😁\n"
                           f"3. А еще могу тебе кидать мемчики на команду /mem\n"
                           f"Будем надеяться что подборка мемов будет расширяться\n"
                           f"4. И последнее, это команда game выдает разные эмодзи игр")


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


@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_file_id(message: Message):
    await message.reply(message.photo[-1].file_id)


async def send_photo(message: Message):
    chat_id = message.from_user.id

    photo_bytes1 = InputFile(path_or_bytesio='media/proga.jpeg')
    photo_bytes2 = InputFile(path_or_bytesio='media/proga2.jpg')
    photo_bytes3 = InputFile(path_or_bytesio='media/proga3.jpg')

    await dp.bot.send_photo(chat_id=chat_id, photo=photo_bytes1)
    await dp.bot.send_photo(chat_id=chat_id, photo=photo_bytes2)
    await dp.bot.send_photo(chat_id=chat_id, photo=photo_bytes3)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(send_photo, commands=['mem'])