from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F
import json
import random

router = Router()


def get_place_of_the_day():
    with open('travel_bot/assets/data_places.json', 'r', encoding='utf-8') as f:
        data_places = json.load(f)
    place_id = random.randint(1, 88)
    header = data_places[place_id - 1]["h3"].replace('/', '-', 1).replace('/', '', 2)
    message = f'<b>{header}</b>\n\n{data_places[place_id - 1]["p"]}'
    return message

@router.message(F.text.lower() == "место дня")
async def send_place_of_the_day(message: Message):
    message_answer = get_place_of_the_day()
    await message.reply(message_answer)