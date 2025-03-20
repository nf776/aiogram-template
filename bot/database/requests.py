from bot.database.models import async_session
from bot.database.models import User
from sqlalchemy import select


# регистрация пользователя если выполнены все условия
async def add_user(telegram_id):
    async with async_session() as session:
        user = await session.scalar(select(User.id).where(
            User.telegram_id == telegram_id
            )
        )
        
        if not user:
            session.add(User(telegram_id=telegram_id))
            await session.commit()
        else:
            return False

# получение списка всех telegram_id юзеров
async def get_all_users() -> list:
    async with async_session() as session:
        user = await session.execute(select(User.telegram_id))
        return user.scalars().all()

# проверка на существование пользователя в базе
async def if_user_exist(telegram_id) -> bool:
    async with async_session() as session:
        query = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        # results = await session.execute(query)
        if query:
            return True
        else:
            return False

# получение telegram_id определенного пользователя
async def get_user_id(telegram_id):
    async with async_session() as session:
        query = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        telegram_id = query.telegram_id
        if telegram_id:
            return telegram_id
        else:
            return 0