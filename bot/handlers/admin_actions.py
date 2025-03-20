from aiogram import Router, F
from bot.filters.is_owner import IsAdminFilter


router = Router()
router.message.filter(F.chat.type == "private", IsAdminFilter(is_admin=True)) # обработка сообщений только от админов

