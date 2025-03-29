from aiogram import F, Router
from aiogram.filters import MagicData
from aiogram.types import Message, CallbackQuery
from fluent.runtime import FluentLocalization
from datetime import datetime, timezone
from config_reader import config


router = Router()
router.message.filter(MagicData(F.maintenance_mode.is_(True)))
router.callback_query.filter(MagicData(F.maintenance_mode.is_(True)))

l10n = FluentLocalization
msg = l10n.format_value(
    msg_id='maintenance-id',
    args={
        'asctime': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S'),
        'supportbot': config.support_bot
    }
)


@router.message()
async def any_message_in_m_mode(message: Message):
    await message.answer(text=msg)

@router.callback_query()
async def any_callback_in_m_mode(callback: CallbackQuery):
    await callback.message.answer(text=msg)
