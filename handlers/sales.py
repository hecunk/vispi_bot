import asyncio
from bot import dis, vikkipo_class
from states import States
from keyboards import *
from aiogram import types
from aiogram import F
from aiogram.fsm import state
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from handlers.start import *


@dis.callback_query(F.data == 'sales')
async def sales_message(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(States.sales_wait)
    await callback.message.edit_text(f'{vikkipo_class.text}', reply_markup=back_button())


@dis.callback_query(StateFilter(States.sales_wait), F.data == 'back')
async def sales_message(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(States.normal)
    await start_message(callback.message)