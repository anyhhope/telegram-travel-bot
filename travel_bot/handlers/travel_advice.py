from aiogram import Router
from aiogram.types import Message
from aiogram import F
import json
import random
from aiogram.types import FSInputFile


router = Router()

def get_advice():
    with open('travel_bot/assets/data_advice.json', 'r', encoding='utf-8') as f:
        data_advice = json.load(f)
    advice_id = random.randint(0, len(data_advice) - 1)
    message = '<b>Советы по путешествиям!</b>✈\n\n'
    for i, list in enumerate(data_advice[advice_id]):
        message += str(i + 1)+ '. ' + list + '\n\n'
    return message

@router.message(F.text.lower() == "советы по путешествиям")
async def send_travel_advice(message: Message):
    message_answer = get_advice()
    await message.answer(message_answer)