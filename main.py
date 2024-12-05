import logging  # config.py
from aiogram import types, executor
from config import bot, dp
import logging
from aiogram import Bot, Dispatcher
from decouple import config

token = config("TOKEN")

bot = Bot(token=token)
dp = Dispatcher(bot=bot)
import os


@dp.message_handler(commands=["start", "help"])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Приветики {message.from_user.first_name})\n'
                                f'А у меня твой Телеграм ID) - {message.from_user.id}')


@dp.message_handler(commands=["mem"])
async def mem_handler(message: types.Message):
    photo_path = os.path.join('media', 'omg,png')
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo=photo, caption='Как узнать свой id?')


@dp.message_handler()
async def echo_handler(message: types.Message):
    # На случай если сообщение - число
    try:
        number = float(message.text)
        squared = number ** 2
        await message.answer(f"Число {number} в квадрате: {squared}")
    except ValueError:
        # Ну а если нет, то отправляем (эхооо)
        await message.answer(message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
