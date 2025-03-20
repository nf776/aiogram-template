from aiogram import Dispatcher

from bot.fluent_loader import get_fluent_localization
from bot.middlewares import L10nMiddleware, Throttling, DatabaseSession
from bot.database.models import async_session
from config_reader import config


locale = get_fluent_localization()


dp = Dispatcher()

# Смотрим в env включен ли режим обслуживания
dp['maintenance_mode'] = config.maintenance_mode


dp.message.outer_middleware(L10nMiddleware(locale))
dp.pre_checkout_query.outer_middleware(L10nMiddleware(locale))
dp.callback_query.outer_middleware(L10nMiddleware(locale))
dp.message.middleware(Throttling())
dp.update.middleware(DatabaseSession(session_pool=async_session))