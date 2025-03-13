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
from handlers import purchase
import items
from handlers import photo


@dis.callback_query(StateFilter(States.service_wait), F.data == 'cards')
async def cards_message(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(States.service_item_wait)
    await callback.message.edit_text('Выберите тип расклада:', reply_markup=cards_keyboard())


@dis.callback_query(StateFilter(States.service_item_wait), F.data == 'individual_question')
async def individual_cards_message(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(States.cards_wait)
    await state.update_data(purchase_type=callback.data, back_type='cards')
    await callback.message.edit_text(f'{items.ind_cards}', reply_markup=back_purchase_button(), parse_mode=ParseMode.HTML)


@dis.callback_query(StateFilter(States.service_item_wait), F.data == 'normal_cards')
async def normal_cards_message(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(States.cards_wait)
    await callback.message.edit_text('Выберите действие:', reply_markup=back_purchase_cards_button())

@dis.callback_query(StateFilter(States.cards_wait), F.data == 'purchase')
async def purchase_message(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(States.purchase_data_wait)
    await callback.message.edit_text('Введите свое имя, дату рождения и ТИП РАСКЛАДА (если вопрос индивидуальный, то сам вопрос) через запятую!!(обязательно), в формате: Ваня, 27.07.2006, Расклад на месяц', reply_markup=back_button())
    

@dis.message(StateFilter(States.purchase_data_wait))
async def purchase_confirm(message: types.Message, state: FSMContext):
    try:
        await purchase.purchase_handle(message, state, message.text.split(',')[0], message.text.split(',')[1], message.text.split(',')[2], f'@{message.from_user.username}')
        await state.set_state(States.service_wait)
        await message.answer('Покупка сделана успешно!!!, виккипо скоро свяжется с вами! ', reply_markup=back_button())
    except:
        await message.answer('Что-то пошло не так, попробуйте заново, не забывайте про формат: [ВАШЕ_ИМЯ], [ДАТА РОЖДЕНИЯ], [ТИП ПОКУПКИ]', reply_markup=back_button())


@dis.callback_query(StateFilter(States.cards_wait), F.data == 'back')
async def cards_back(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(States.service_wait)
    await cards_message(callback, state)