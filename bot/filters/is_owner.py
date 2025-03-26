from aiogram.filters import BaseFilter
from aiogram.types import Message

from config_reader import config

class IsOwnerFilter(BaseFilter):
    def __init__(self, is_owner):
        self.is_owner = is_owner

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in config.owner_id