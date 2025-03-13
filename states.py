from aiogram.fsm.state import State, StatesGroup


class States(StatesGroup):
    normal = State()
    review_wait = State()
    review_write_wait = State()
    service_wait = State()
    service_item_wait = State()
    service_matrix_item_wait = State()
    additional_services_items_wait = State()
    chakra_items_wait = State()
    cards_wait = State()
    normal_cards_items_wait = State()
    VIKKIPO_STATE = State()
    purchase_data_wait = State()
    sales_wait = State()

