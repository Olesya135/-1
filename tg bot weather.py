import datetime
import logging
import math
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# настройка логирования(для отслеживания событий)
logging.basicConfig(level=logging.INFO)

# Инициализация бота с токеном
bot = Bot(token='7725565955:AAF5Dnh5f8ummbh0HZr1NnpMN2jqDwkkz4g')
dp = Dispatcher(bot)

# Установка команд по умолчанию для бота
async def set_default_commands(dp):
    await dp.bot.set_my_commands([types.BotCommand("start", "Запустить бота"), types.BotCommand("help", "Помощь"),])
    
# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Напиши мне название города и я пришлю сводку погоды")
    
# Обработчик команды /help
@dp.message_handler(commands=['help'])
async def set_default_commands(message: types.Message):
    await message.reply(f"/start\n"
                        f"/help\n")
# Обработчик всех остальных сообщений
@dp.message_handler()
async def echo(message: types.Message):
    city = message.text
    try:
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&units=metric&appid=37c9df52881823df88f0064b3ffa4574")
         # Проверка на ошибки HTTP
        response.raise_for_status()

        # Преобразование ответа в JSON
        data = response.json()
        city = data["name"]
        cur_temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        
        # Формирование и отправка ответа с погодой
        await message.reply(f"{datetime.datetime.now().strftime('%d-%m-%Y %H:%M')}\n"
                             f"Погода в городе: {city}\nТемпература: {cur_temp}°C\n"
                             f"Влажность: {humidity}%\nДавление: {math.ceil(pressure / 1.333)} мм.рт.ст\n"
                             f"Ветер: {wind} м/с\n")
    # Обработка ошибок
    except requests.exceptions.RequestException as e:
        await message.reply(f"Ошибка при запросе к API: {e}")
    except KeyError as e:
        await message.reply(f"Неверный формат ответа от API: {e}")
    except Exception as e:
        await message.reply(f"Непредвиденная ошибка: {e}")
# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
