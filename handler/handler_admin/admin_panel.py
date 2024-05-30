from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F

from keyboard.callback import admin
from config import ADMINS

router = Router()


@router.message(F.from_user.id.in_(ADMINS) and Command("admin"))
async def admin_panel(msg: Message):
    await msg.answer("Админ панель", reply_markup=admin)
