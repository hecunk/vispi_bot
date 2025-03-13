import asyncio
from bot import dis, bt
from states import States
from keyboards import *
from aiogram import types
from aiogram import F
from aiogram.fsm import state
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.enums.parse_mode import ParseMode
from handlers.start import *


@dis.callback_query(StateFilter(States.normal), F.data == 'review')
async def review_message(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(States.review_wait)
    await callback.message.edit_text('Выберите действие:', reply_markup=review_keyboard())


@dis.callback_query(StateFilter(States.review_wait), F.data == 'leave_review')
async def review_leave_message(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(States.review_write_wait)
    await callback.message.edit_text('Здесь Вы можете написать пожелания, отзыв и моменты, которые я могу улучшить в работе 💗🫂', reply_markup=back_button())


@dis.message(StateFilter(States.review_write_wait))
async def review_sendler(message: types.Message, state: FSMContext):
    await bt.send_message(723458129, f'''ВИККИПО НОВЫЙ ОТЗЫВ ОТ: @{message.from_user.username}
ОТЗЫВ: {message.text}''')
    await message.answer('Спасибо, что воспользовались моими услугами, <b>Ваш отзыв поможет стать мне лучше</b> 💗🎀', reply_markup=back_button(), parse_mode=ParseMode.HTML)
    await state.set_state(States.review_wait)


@dis.callback_query(StateFilter(States.review_write_wait), F.data == 'back')
async def review_write_back(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(States.review_wait)
    await review_message(callback, state)


@dis.callback_query(StateFilter(States.review_wait), F.data == 'back')
async def review_back(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(States.normal)
    await start_message(callback.message)