from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def start_keyboard():
    buttons = [[InlineKeyboardButton(text='Отзывы', callback_data='review'), InlineKeyboardButton(text='Услуги', callback_data='services')], [InlineKeyboardButton(text='Акции', callback_data='sales')]]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def review_keyboard():
    buttons = [[InlineKeyboardButton(text='Посмотреть отзывы', url='https://t.me/vispireviews'), InlineKeyboardButton(text='Оставить отзыв', callback_data='leave_review')], [InlineKeyboardButton(text='Вернуться', callback_data='back')]]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def services_keyboard():
    buttons = [[InlineKeyboardButton(text='Матрица', callback_data='matrix'), InlineKeyboardButton(text='Расклады', callback_data='cards'), InlineKeyboardButton(text='Чакры', callback_data='chakra')], [InlineKeyboardButton(text='Вернуться', callback_data='back')]]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def matrix_keyboard():
    buttons = [[InlineKeyboardButton(text='Судьба', callback_data='fate_matrix'), InlineKeyboardButton(text='Совместимость', callback_data='compatability_matrix')], [InlineKeyboardButton(text='Вернуться', callback_data='back')]]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def chakra_keyboard():
    buttons = [[InlineKeyboardButton(text='Чакроанализ', callback_data='chakra_purchase'), InlineKeyboardButton(text='Камни', callback_data='stones')], [InlineKeyboardButton(text='Вернуться', callback_data='back')]]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def cards_keyboard():
    buttons = [[InlineKeyboardButton(text='Индивидуальный вопрос', callback_data='individual_question'), InlineKeyboardButton(text='Обычные расклады', callback_data='normal_cards')], [InlineKeyboardButton(text='Вернуться', callback_data='back')]]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def back_purchase_button():
    buttons = [[InlineKeyboardButton(text='Сделать заказ', callback_data='purchase')], [InlineKeyboardButton(text='Вернуться', callback_data='back')]]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def back_purchase_cards_button():
    buttons = [[InlineKeyboardButton(text='Посмотреть расклады', url='https://t.me/+1vi__IASSadlN2My'), InlineKeyboardButton(text='Сделать заказ', callback_data='purchase')], [InlineKeyboardButton(text='Вернуться', callback_data='back')]]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def back_button():
    buttons = [[InlineKeyboardButton(text='Вернуться', callback_data='back')]]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def vikkipo_keyboard():
    buttons = [[InlineKeyboardButton(text='ИЗМЕНИТЬ АКЦИИ', callback_data='change_sales')]]
    return InlineKeyboardMarkup(inline_keyboard=buttons)