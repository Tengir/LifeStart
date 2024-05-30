import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import config
from middleware import AlbumMiddleware
from handler.handler_user import routers as routers_user
from handler.handler_admin import routers as routers_admin


async def main():
    bot = Bot(token=config.TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.channel_post.middleware(AlbumMiddleware())
    # Добавляем роутер пользовательский и админский.
    for router in routers_admin:
        dp.include_router(router)
    for router in routers_user:
        dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())