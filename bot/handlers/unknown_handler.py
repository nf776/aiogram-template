from aiogram import Router
from aiogram.types import Message
from bot.fluent_loader import FluentLocalization

router = Router()

@router.message()
async def unknown_cmd(message: Message, l10n: FluentLocalization):
    await message.reply(l10n.format_value('unknown-cmd'))