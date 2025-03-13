import asyncio
import aiogram
from bot import dis, vikkipo_class
from states import States
from keyboards import *
from aiogram import types
from aiogram import F
from aiogram.fsm import state
from aiogram.filters import StateFilter, CommandStart
from aiogram.fsm.context import FSMContext


@dis.message(F.text == 'руслан гасанов самый (НЕ)приятный человек в конфе)))')
async def vikkipo_handler(message: types.Message, state: FSMContext):
    await state.set_state(States.VIKKIPO_STATE)
    await message.answer('ВИККИПО ПРИВЕТ ТЫ В СИСТЕМЕ, чтобы вернутся в ОБЫЧНЫЙ РЕЖИМ пиши /start', reply_markup=vikkipo_keyboard())


@dis.callback_query(StateFilter(States.VIKKIPO_STATE), F.data == 'change_sales')
async def change_sales_message(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(States.sales_wait)
    await callback.message.edit_text('ВИМККИ ПОДНИКИ НАПИШИТЕ КА ВАШИ НЯШНЫЕ АКЦИИ)))))))))))))))))')


@dis.message(StateFilter(States.sales_wait))
async def change_sales(message: types.Message, state: FSMContext):
    vikkipo_class.text = message.text
    await state.set_state(States.VIKKIPO_STATE)
    await message.answer('ВИКЕПО ПОЗДРАВЛЯЮ ТЫ ИЗМЕНИЛА АКЦИИ КАКАЯ ЖЕ ТЫ МОЛОДЕЦ ВИКА ПРОСТО МОЛОДДЧИНА БЛЯТЬ', reply_markup=back_button())


@dis.callback_query(StateFilter(States.VIKKIPO_STATE), F.data == 'back')
async def change_sales_back(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text('ВИККИПО ПРИВЕТ ТЫ В СИСТЕМЕ, чтобы вернутся в ОБЫЧНЫЙ РЕЖИМ пиши /start', reply_markup=vikkipo_keyboard())