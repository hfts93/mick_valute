import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import CommandStart
from aiogram.types.web_app_info import WebAppInfo


bot = Bot('6480088620:AAEUzV7WSGoNS1po77CgjciXw792INGQMHQ')
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)



@dp.message(CommandStart())
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(keyboard=[
        [types.KeyboardButton(text="Открыть веб старницу", web_app=WebAppInfo(url='https://c781-217-13-216-145.ngrok-free.app'))]
    ])
    await message.answer(text='Привет, пользователь!', reply_markup=markup)


if __name__ == "__main__":
    asyncio.run(main=main())
    print("Бот запущен успешно")