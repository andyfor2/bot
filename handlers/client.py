from aiogram import types, Dispatcher
from create_bot import bot, dp


async def registration(message : types.Message):
    if message.chat.type == "private": #Сделать проверку есть ли человек в базе данных
        await bot.send_message(message.from_user.id, 'Вы успешно прошли регистрацию!\nНапишите "Помощь"') #+База данных
    else:
       await message.answer('Пройдите регистрацию в ЛС с ботом\nhttps://t.me/duxyplay_bot')

def register_handlers_client(dp : Dispatcher):
    def check(msg):
        list = ['/start', 'регистрация']
        return msg.text.lower() in list
    dp.register_message_handler(registration, check)
