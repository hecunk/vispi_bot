import asyncio
from bot import dis
from states import States
from keyboards import *
from aiogram import types
from aiogram import F
from aiogram.fsm import state
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from handlers.start import *
from handlers import matrix, cards, chakra, purchase


def back_filter(callback, state, item):
    items = ['matrix', 'chakra', 'cards']
    if items.index(item) == 0:
        return matrix.matrix_message(callback, state)
    if items.index(item) == 1:
        return chakra.chakra_message(callback, state)
    if items.index(item) == 2:
        return cards.cards_message(callback, state)



@dis.callback_query(StateFilter(States.normal), F.data == 'services')
async def services_message(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(States.service_wait)
    await callback.message.edit_text('Выберите услугу: ', reply_markup=services_keyboard())


@dis.callback_query(StateFilter(States.service_item_wait), F.data == 'back')
async def back_to_services(callback: types.CallbackQuery, state: FSMContext):
    await services_message(callback, state)


@dis.callback_query(F.data == 'purchase')
async def purchase_message(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(States.purchase_data_wait)
    await callback.message.edit_text('Введите свое имя и дату рождения через запятую!!(обязательно), в формате: Ваня, 27.07.2006', reply_markup=back_button())
    

@dis.message(StateFilter(States.purchase_data_wait))
async def purchase_confirm(message: types.Message, state: FSMContext):
    try:
        await purchase.purchase_handle(message, state, message.text.split(',')[0], message.text.split(',')[1], (await state.get_data())['purchase_type'], f'@{message.from_user.username}')
        await state.set_state(States.service_wait)
        await message.answer('Покупка сделана успешно!!!, ждите викепо', reply_markup=back_button())
    except:
        await message.answer('Что-то пошло не так, попробуйте заново, не забывайте про формат: [ВАШЕ_ИМЯ], [ДАТА РОЖДЕНИЯ]', reply_markup=back_button())


@dis.callback_query(StateFilter(States.purchase_data_wait), F.data == 'back')
async def back_from_purchase(callback: types.CallbackQuery, state: FSMContext):
    await back_filter(callback, state, (await state.get_data())['back_type'])


@dis.callback_query(StateFilter(States.service_wait), F.data == 'back')
async def back_to_start(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(States.normal)
    await start_message(callback.message)