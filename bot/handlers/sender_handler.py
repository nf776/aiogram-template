import time
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.exceptions import TelegramBadRequest
from fluent.runtime import FluentLocalization
from bot.filters.is_owner import IsOwnerFilter
from bot.states.sender_state import CreateSenderMessage
from bot.utils import sender_core
from bot.keyboards.sender_inline import get_kb_confirm
from sqlalchemy.ext.asyncio import AsyncSession
from bot.__main__ import bot
from bot.database.requests import get_all_users

router = Router()
router.message.filter(F.chat.type == "private", IsOwnerFilter(is_owner=True)) # обработка сообщений только от админов


@router.message(Command(commands=["sender"]))
async def create_sender_handler(message: Message, state: FSMContext, l10n: FluentLocalization) -> None:
    await message.answer(l10n.format_value('sender-text'))
    await state.set_state(CreateSenderMessage.get_text)


@router.message(CreateSenderMessage.get_text, F.text)
async def set_text_handler(message: Message, state: FSMContext, l10n: FluentLocalization):
    await state.update_data(msg_text=message.md_text)
    await message.answer(l10n.format_value('sender-photo'))
    await state.set_state(CreateSenderMessage.get_photo)


@router.message(CreateSenderMessage.get_photo, F.photo)
async def set_photo_handler(message: Message, state: FSMContext, l10n: FluentLocalization):
    await state.update_data(msg_photo=message.photo[-1].file_id)
    await state.set_state(CreateSenderMessage.get_keyboard_text)
    await message.answer(l10n.format_value('sender-button-text'))


@router.message(CreateSenderMessage.get_keyboard_text, F.text)
async def set_btn_text_handler(message: Message, state: FSMContext, l10n: FluentLocalization):
    await state.update_data(btn_text=message.text)
    await state.set_state(CreateSenderMessage.get_keyboard_url)
    await message.answer(l10n.format_value('sender-button-url'))


@router.message(CreateSenderMessage.get_keyboard_url, F.text)
async def set_btn_url_handler(message: Message, state: FSMContext, l10n: FluentLocalization):
    try:
        await state.update_data(btn_url=message.text)
        data = await state.get_data()
        message_id = await sender_core.send_preview(
            message,
            data
        )
        await state.update_data(message_id=message_id)
        await message.answer(
            text=l10n.format_value('sender-confirmation'),
            reply_markup=get_kb_confirm().as_markup(),
        )
        await state.set_state(CreateSenderMessage.confirm_sender)
    except TelegramBadRequest:
        await message.answer(l10n.format_value('sender-telegrambadrequest'))


@router.callback_query(F.data == 'cancel_sender', CreateSenderMessage.confirm_sender)
async def cancel_sending(callback: CallbackQuery, state: FSMContext, l10n: FluentLocalization):
    await callback.message.edit_text(l10n.format_value('sender-cancel'))
    await state.clear()
    await callback.answer()


@router.callback_query(F.data == 'start_sender', CreateSenderMessage.confirm_sender)
async def start_sending(callback: CallbackQuery, state: FSMContext, session: AsyncSession, l10n: FluentLocalization):
    data = await state.get_data()
    await callback.message.answer(l10n.format_value('sender-started'))
    await state.clear()
    await callback.answer()

    user_ids = await get_all_users()
    t_start = time.time()
    message_id = data.get('message_id')
    count = await sender_core.start_sender(
        session=session,
        bot=bot,
        data=data,
        user_ids=user_ids,
        from_chat_id=callback.message.chat.id,
        message_id=message_id)
    await callback.message.answer(
        l10n.format_value(
            msg_id='sender-info',
            args={
                'count': count,
                'users_count': len(user_ids),
                'sendtime': round(time.time() - t_start)
            }
        )
    )