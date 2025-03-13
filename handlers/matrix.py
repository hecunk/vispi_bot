import asyncio
from bot import dis
from states import States
from keyboards import *
from aiogram import types
from aiogram import F
from aiogram.fsm import state
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.enums.parse_mode import ParseMode
import items


@dis.callback_query(StateFilter(States.service_wait), F.data == 'matrix')
async def matrix_message(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(States.service_item_wait)
    await callback.message.edit_text('Выберите матрицу:', reply_markup=matrix_keyboard())


@dis.callback_query(StateFilter(States.service_item_wait), F.data == 'fate_matrix')
async def fate_matrix_message(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(States.service_matrix_item_wait)
    await state.update_data(purchase_type=callback.data, back_type='matrix')
    await callback.message.edit_text(f'{items.mat_fate}', reply_markup=back_purchase_button(), parse_mode=ParseMode.HTML)


@dis.callback_query(StateFilter(States.service_item_wait), F.data == 'compatability_matrix')
async def compatability_matrix_message(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(States.service_matrix_item_wait)
    await state.update_data(purchase_type=callback.data, back_type='matrix')
    await callback.message.edit_text(f'{items.mat_com}', reply_markup=back_purchase_button(), parse_mode=ParseMode.HTML)


@dis.callback_query(StateFilter(States.service_matrix_item_wait), F.data == 'back')
async def matrix_back(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(States.service_wait)
    await matrix_message(callback, state)