from aiogram.fsm.state import StatesGroup, State


class CreateSenderMessage(StatesGroup):
    get_text = State()
    get_photo = State()
    get_keyboard_text = State()
    get_keyboard_url = State()
    confirm_sender = State()