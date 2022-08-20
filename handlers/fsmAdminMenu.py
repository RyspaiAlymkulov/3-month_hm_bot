from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, ADMIN
from keyboards.client_kb import cancel_markup
from database import bot_db


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


async def fsm_start(message: types.Message):
    if message.chat.type == "private" and message.from_user.id == ADMIN:
        await message.reply(f"Привет, рад тебя видеть {message.from_user.full_name}")
        await FSMAdmin.photo.set()
        await message.answer(f"я жду от тебя фотографию меню",
                             reply_markup=cancel_markup)

    else:
        await message.reply("Ты не администратор")


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer("Название блюда")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Описание блюда")


async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.answer("Цена блюда")


async def load_price(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['price'] = int(message.text)
        await bot.send_photo(message.from_user.id,
                             data['photo'],
                             caption=f"Блюдо: {data['name']}\n"
                                     f"Описание: {data['description']}\n"
                                     f"Цена: {data['price']}\n")
        await bot_db.sql_command_insert(state)
        await state.finish()
        await message.answer("регистрация окончена")
    except:
        await message.reply("только числа")


async def cancel_registration(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer("регистрация отменена")


async def delete_data(message: types.Message):
    users = await bot_db.sql_command_all()
    for user in users:
        await bot.send_photo(message.from_user.id,
                             user[0],
                             caption=f"Блюдо: {user[1]}\n"
                                     f"Описание: {user[2]}\n"
                                     f"Цена: {user[3]}\n",
                             reply_markup=InlineKeyboardMarkup().add(
                                 InlineKeyboardButton(
                                     f"delete {user[1]}",
                                     callback_data=f"delete {user[1]}"
                                 )
                             ))


async def complete_delete(call: types.CallbackQuery):
    await bot_db.sql_command_delete(call.data.replace("delete ", ""))
    await call.answer(text="Ваше меню удалено из базы данных",  show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)


def register_handlers_fsm_menu(dp: Dispatcher):
    dp.register_message_handler(cancel_registration, state='*', commands="cancel")
    dp.register_message_handler(cancel_registration,
                                Text(equals='cancel', ignore_case=True),
                                state='*')
    dp.register_message_handler(fsm_start, commands=['menu'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo,
                                content_types=['photo'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_callback_query_handler(
        complete_delete,
        lambda call: call.data and call.data.startswith("delete ")
    )

