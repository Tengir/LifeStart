from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram import F

from config import ADMINS

from state import AdminState

router = Router()


@router.callback_query(F.from_user.id.in_(ADMINS), F.data == "set_faq")
async def wait_faq(callback: CallbackQuery, state: FSMContext):
    await state.set_state(AdminState.set_faq)

    await callback.message.edit_text(text="Напишите новый FAQ")
