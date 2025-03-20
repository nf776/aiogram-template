import bot.database.requests as db
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from fluent.runtime import FluentLocalization

router = Router()
router.message.filter(F.chat.type == "private")

@router.message(Command("start"))
async def cmd_hello(message: Message, l10n: FluentLocalization):
    await db.add_user(message.from_user.id)
    await message.answer(l10n.format_value("hello-msg"))

