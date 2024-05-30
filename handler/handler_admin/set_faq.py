from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import F

from config import ADMINS

from state import AdminState

from utils.change_faq import change_faq

router = Router()


@router.message(F.from_user.id.in_(ADMINS), StateFilter(AdminState.set_faq))
async def set_faq(msg: Message, state: FSMContext):
    await state.clear()
    new_faq = msg.text
    change_faq(new_faq)
    await msg.answer(f"Готово\n{new_faq}")
