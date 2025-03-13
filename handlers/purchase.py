from handlers import review, services
import asyncio
from bot import dis, bt
from states import States
from keyboards import *
from aiogram import types
from aiogram import F
from aiogram.fsm import state
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext


@dis.callback_query(StateFilter(States.purchase_data_wait), F.data == 'purchase_handle')
async def purchase_handle(callback: types.CallbackQuery, state: FSMContext, name: str, age: int, type: str, id: str):
    await bt.send_message(723458129, f'''ВИКЕПО ПОЗДРАВЛЯЮ НОВАЯ ПОКУПКА!!!! 
ИМЯ: {name},
ДАТА РОЖДЕНИЯ: {age},
ТИП ПОКУПКИ: {type},
ТГ: {id}                   
''')



