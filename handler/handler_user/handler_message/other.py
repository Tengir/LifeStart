from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def digest(msg: Message):
    await msg.answer(f"Что-то пошло не так...")
