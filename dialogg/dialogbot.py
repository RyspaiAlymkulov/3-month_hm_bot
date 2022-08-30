# import os
# from google.cloud import dialogflow
# from aiogram import bot, types
# from aiogram.bot import bot
# from config import dp, bot
#
#
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'ssmalltalk-hhsb-bf46e7e795eaaa.json'
#
#
# session_client = dialogflow.SessionsClient()
# project_id = 'ssmalltalk-hhsb'
# session_id = 'sessions'
# language_code = 'ru'
# session = session_client.session_path(project_id, session_id)
#
#
# @dp.message_handler(commands=['dialog'])
# async def send_welcome(message: types.Message):
#     await bot.send_message(message.from_user.id, text=f"Привет {message.from_user.full_name}.\n Я конечно тупой как пробка,"
#                                                       f"но мы можем поговорить")
#
#
# @dp.message_handler()
# async def lzt_dialogflow(message: types.Message):
#     text_input = dialogflow.TextInput(
#             text=message.text, language_code=language_code)
#     query_input = dialogflow.QueryInput(text=text_input)
#     response = session_client.detect_intent(
#         session=session, query_input=query_input)
#     if response.query_result.fulfillment_text:
#         await bot.send_message(message.from_user.id, response.query_result.fulfillment_text)
#     else:
#         await bot.send_message(message.from_user.id, "Я тебя не понимаю")
#
#
#
