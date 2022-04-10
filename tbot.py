import requests
import telebot
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token ='9bdb588bbe6b4e7884a105739220804'
tel_token = '5265118363:AAEf_bYyFbrAjJ0BhulFGyEs1orBS3xRmQI'

Bot = Bot(token=tel_token)
dp = Dispatcher(Bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Type city name <3")

@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f"http://api.weatherapi.com/v1/current.json?key={token}&q={message.text}"
        )
        data = r.json()
        #pprint(data)
        temp_c = data['current']['temp_c']
        feelslike_c = data['current']['feelslike_c']
        wind_s = round(int(data['current']['wind_kph']) / 3.6, 2)

        await message.reply(
              f"Температура: {temp_c}C°\n"
              f"Ощущается как: {temp_c}C°\n"
              f"Ветер: {wind_s} м/с"
              )

    except Exception as ex:
        await message.reply("Проверьте название города")

if __name__ == '__main__':
    executor.start_polling(dp)
