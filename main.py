import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from datetime import datetime

from app.model import get_congratulation
from app.stickers import get_random_tiger

from config import TOKEN

# Инициализация бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# декоратор
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_name = message.from_user.first_name

    # await = return для async функций
    await message.reply(f'Привет, {user_name}! Чтобы получить персональное поздравление напиши имя получателя.')

@dp.message_handler(commands=['help'])
async def start(message: types.Message):
    await message.reply(f'Чтобы получить персональное поздравление напиши имя получателя.')

@dp.message_handler(content_types=['text'])
async def congratulation(message: types.Message):

    day = datetime.now().day
    month_num = datetime.now().monthe

    check_date = str(month_num) + '-' + ('0' + str(day))[-2:]

    if ('12-01' <= check_date <= '12-31' or '01-01' <= check_date <= '01-10'):
        chat_id = message.chat.id
        tiger_sticker = get_random_tiger()
        await message.reply(get_congratulation(message.text))
        await bot.send_sticker(chat_id, sticker=tiger_sticker)
    else:
        await message.reply(f'Подождите следующий декабрь!')

@dp.message_handler(content_types=['sticker'])
async def load_sticker(message: types.Message):
    chat_id = message.chat.id
    print(message.sticker.file_id)
    await bot.send_sticker(chat_id, sticker=message.sticker.file_id)

# Команда для запуска бота
if __name__ == '__main__': # всегда True
    executor.start_polling(dp)