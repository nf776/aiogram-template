from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat

from config_reader import config


async def set_bot_commands(bot: Bot):
    """
    Установка команд для разных групп пользователей.
    
    """

    
    usercommands = [
        BotCommand(command="start", description="Перезапуск бота."),
    ]
    await bot.set_my_commands(usercommands, scope=BotCommandScopeDefault())

    admin_commands = [
        BotCommand(command="start", description="Перезапуск бота"),
    ]
    for admin in config.owner_id:
        await bot.set_my_commands(
            admin_commands,
            scope=BotCommandScopeChat(chat_id=admin)
        )