from aiogram import types, Dispatcher
from create_bot import bot, dp
from messages import help_txt, need_registration

def is_registered(user): # TODO: Базу данных
        return True
@dp.message_handler(lambda msg: msg.text.lower() in ('/start', 'регистрация'))
async def registration(m: types.Message):
    if m.chat.type == "private": #Сделать проверку есть ли человек в базе данных
        await bot.send_message(m.from_user.id, 'Вы успешно прошли регистрацию!\nНапишите "Помощь"') # TODO: +База данных
    else:
       await message.answer(need_registration)
@dp.message_handler(lambda msg: msg.text.lower() == 'помощь')
async def help_answer(m : types.Message):
    if is_registered(m.from_user.id):
        await bot.send_message(m.from_user.id, help_txt)
    else: 
        await m.answer(need_registration)
