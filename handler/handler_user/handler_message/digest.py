from aiogram import Router
from aiogram.types import Message
from aiogram import F

from data import Data

router = Router()


@router.message(F.text.lower().in_(["дайджест", "digest"]))
async def digest(msg: Message):
    await msg.answer(Data().message.digest)
