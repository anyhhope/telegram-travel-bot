from aiogram import Router
from aiogram.types import Message
from aiogram import F
import json
import random
from aiogram.types import FSInputFile
from datetime import date

router = Router()
user_data = {}

def get_place_of_the_day(user_id):
    with open('travel_bot/assets/data_places.json', 'r', encoding='utf-8') as f:
        data_places = json.load(f)
    
    if user_id in user_data and user_data[user_id]['date'] == date.today():
        place_id = user_data[user_id]['place_id']
    else:
        place_id = random.randint(1, 88)
        user_data[user_id] = {'date': date.today(), 'place_id': place_id}
    
    header = data_places[place_id - 1]["h3"].replace('/', '-', 1).replace('/', '', 2)
    message = f'<b>{header}</b>\n\n{data_places[place_id - 1]["p"]}'
    return message, place_id

@router.message(F.text.lower() == "место дня")
async def send_place_of_the_day(message: Message):
    message_answer, place_id = get_place_of_the_day(message.from_user.id)
    image_from_pc = FSInputFile(f'travel_bot/assets/places_images/img{place_id}.jpg')
    await message.answer_photo(
        image_from_pc,
        caption=message_answer
    )