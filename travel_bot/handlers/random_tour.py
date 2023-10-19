from aiogram import Router
from aiogram.types import Message
from aiogram import F
import json
import random

router = Router()

def get_tour():
    with open('travel_bot/assets/data_tours.json', 'r', encoding='utf-8') as f:
        data_tours = json.load(f)
    tour_id = random.randint(0, len(data_tours) - 1)
    message = f'<b>{data_tours[tour_id]["header"]}</b>\n\n{data_tours[tour_id]["description"]}\nСтоимость: {data_tours[tour_id]["price"]}\n\n<a href="{data_tours[tour_id]["link"]}">Перейти на сайт</a>'
    return message

@router.message(F.text.lower() == "случайное путешествие")
async def send_travel_advice(message: Message):
    message_answer = get_tour()
    await message.answer(message_answer)