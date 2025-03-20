from aiogram.filters import BaseFilter
from aiogram.types import Message

from config_reader import config

class IsAdminFilter(BaseFilter):
    def __init__(self, is_admin):
        self.is_admin = is_admin

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in config.admin_id