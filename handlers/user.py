
import asyncio

from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.dispatcher.filters.state import State, StatesGroup

from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from key.buttons import main_menu, stop_menu
from random import random, randrange, randint


class FSMChat(StatesGroup):
    thing = State()


async def cm_start(message: types.Message):
    await bot.send_message(message.from_user.id, '🤔Что вы хотели найти')
    await FSMChat.thing.set()


async def search_thing(message: types.Message, state: FSMChat):
    text = message.text
    user_id = message.from_user.id

    if text=="❌стоп":
        await state.finish()
        await bot.send_message(user_id, "😊Буду рад если вам помог.")
        await bot.send_message(user_id, "🎊 🎉Что бы искать товар снова нажминте кнопку '🔍 Искать'", reply_markup=main_menu)
    else:
        await bot.send_message(user_id, "Немножко подождите 😉")
        ls_product = randint(0, 1000)
        places_product = randint(0, 1000)
        id_product = randint(10000, 1000000)
        generated_text = f"✔☺{text} \n(идентификатор товара ) - {id_product} находится на {ls_product} настранице на {places_product} месте."
        await bot.send_message(user_id, generated_text)
        await bot.send_message(user_id, "Что то еще хотите найти. Если вы уже нашли то что ичкали нажмите кнопку '❌стоп'", reply_markup=stop_menu)


def register_user(dp : Dispatcher):
    dp.register_message_handler(cm_start, Text(equals='🔍 Искать', ignore_case=True))
    dp.register_message_handler(search_thing, state=FSMChat.thing)