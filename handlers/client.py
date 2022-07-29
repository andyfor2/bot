from aiogram import types, Dispatcher
from create_bot import bot, dp
from messages import help_txt, need_registration



def is_registered(user):
        return True

async def registration(message : types.Message):
    if message.chat.type == "private": #Сделать проверку есть ли человек в базе данных
        await bot.send_message(message.from_user.id, 'Вы успешно прошли регистрацию!\nНапишите "Помощь"') #+База данных
    else:
       await message.answer(need_registration)

async def help_answer(message : types.Message):
    if is_registered:
        await bot.send_message(help_txt)
    else: 
        await bot.send_message(need_registration)

def register_handlers_client(dp : Dispatcher):
    def check(msg):
        list = ['/start', 'регистрация']
        return msg.text.lower() in list
    dp.register_message_handler(registration, check)
