from aiogram import Router, F
from bot.filters.is_owner import IsOwnerFilter


router = Router()
router.message.filter(F.chat.type == "private", IsOwnerFilter(is_owner=True)) # обработка сообщений только от админов

