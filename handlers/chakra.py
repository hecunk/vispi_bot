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


@dis.callback_query(StateFilter(States.service_wait), F.data == 'chakra')
async def chakra_message(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(States.service_item_wait)
    await callback.message.edit_text('Выберите, что вас интересует:', reply_markup=chakra_keyboard())


@dis.callback_query(StateFilter(States.service_item_wait), F.data == 'chakra_purchase')
async def chakra_item_1(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(States.chakra_items_wait)
    await state.update_data(purchase_type=callback.data, back_type='chakra')
    await callback.message.edit_text(f'{items.chakr_anal}', reply_markup=back_purchase_button(), parse_mode=ParseMode.HTML)


@dis.callback_query(StateFilter(States.service_item_wait), F.data == 'stones')
async def stones_message(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(States.chakra_items_wait)
    await state.update_data(purchase_type=callback.data, back_type='chakra')
    await callback.message.edit_text(f'{items.stones}', reply_markup=back_purchase_button(), parse_mode=ParseMode.HTML)


@dis.callback_query(StateFilter(States.chakra_items_wait), F.data == 'back')
async def chakra_back(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(States.service_wait)
    await chakra_message(callback, state)