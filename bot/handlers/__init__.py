from aiogram import Router


def setup_routers() -> Router:
    from . import admin_actions, maintenance_mode, personal_actions, sender_handler, unknown_handler

    router = Router()
    router.include_routers(
        maintenance_mode.router,
        sender_handler.router,
        admin_actions.router,
        personal_actions.router,
        unknown_handler.router
    )

    return router