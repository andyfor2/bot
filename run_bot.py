from aiogram import executor, types
from create_bot import dp, bot
from handlers import admin, client, other, games

print('Бот запустился')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
