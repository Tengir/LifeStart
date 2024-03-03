from aiogram import Router
from aiogram.types import Message
from aiogram import F

from data import Data
from keyboard.reply import menu

router = Router()


@router.message(F.text.lower().in_(["faq", "вопросы", "частые вопросы"]))
async def faq(msg: Message):
    await msg.answer(Data().message.faq, reply_markup=menu)
