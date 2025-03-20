import asyncio
import logging
from contextlib import suppress
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from bot.utils.tg_commands import set_bot_commands
from config_reader import config
from bot.dispatcher import dp
from bot.database.models import connect_db
from bot.handlers import setup_routers


bot = Bot(
    token=config.bot_token.get_secret_value(),
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)


async def main():
    await connect_db()
    await bot.delete_webhook(drop_pending_updates=True)
    await set_bot_commands()

    routers = setup_routers()
    dp.include_router(routers)

    try:
        await dp.start_polling(bot, skip_updates=False) # Если используем платежки НЕ ПРОПУСКАЕМ АПДЕЙТЫ
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="DEV BOT - %(asctime)s - %(levelname)s - %(name)s - %(message)s")
    with suppress(KeyboardInterrupt):
            asyncio.run(main())
