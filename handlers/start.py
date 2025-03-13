import asyncio
import aiogram
from bot import dis
from states import States
from keyboards import *
from aiogram import types
from aiogram import F
from aiogram.fsm import state
from aiogram.filters import StateFilter, CommandStart
from aiogram.fsm.context import FSMContext
import items


@dis.message(CommandStart())
async def start(message: types.Message, state: FSMContext):
    await state.set_state(States.normal)
    await message.answer(f'{items.strt}', reply_markup=start_keyboard())


async def start_message(message: types.Message):
    await message.edit_text(f'{items.strt}', reply_markup=start_keyboard())


@dis.message(~StateFilter(States.purchase_data_wait), ~StateFilter(States.review_write_wait), ~StateFilter(States.sales_wait), F.text != 'руслан гасанов самый приятный человек в конфе')
async def not_valid_message(message: types.Message, state: FSMContext):
    await message.answer('извини я не понимаю напиши /start')


@dis.message(F.text == 'руслан гасанов самый приятный человек в конфе')
async def vikkipo_handler(message: types.Message, state: FSMContext):
    await state.set_state(States.VIKKIPO_STATE)
    await message.answer('ВИККИПО ПРИВЕТ ТЫ В СИСТЕМЕ, чтобы вернутся в ОБЫЧНЫЙ РЕЖИМ пиши /start', reply_markup=vikkipo_keyboard())

from handlers import review, services, sales, vikkipo