# Главное меню, вызывается на старт ил меню. Также можно перейти в него из
# Дайджеста по reply кнопке ВЕРНУТЬСЯ В ГЛАВ МЕНЮ,
# Ответы и результат(после завершения теста) по reply кнопке ВЕРНУТЬСЯ В ГЛАВ МЕНЮ.
# Есть аналогичная кнопка в callback.

from aiogram import Router
from aiogram.types import Message
from aiogram import F

import keyboard.reply
from data import Data

router = Router()


@router.message(F.text.lower().in_(["/start", "меню", "вернуться в меню", "назад", "назад в меню"]))
async def menu_message(msg: Message):
    await msg.answer(Data().message.menu, reply_markup=keyboard.reply.menu)
