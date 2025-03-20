from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_kb_confirm() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Запустить рассылку", callback_data=f"start_sender")
    )
    builder.row(
        InlineKeyboardButton(text="Отменить", callback_data=f"cancel_sender")
    )
    return builder