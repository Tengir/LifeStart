from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram import F

from config import ADMINS

from state import AdminState

router = Router()


@router.callback_query(F.from_user.id.in_(ADMINS), F.data == "set_table")
async def wait_table(callback: CallbackQuery, state: FSMContext):
    await state.set_state(AdminState.set_table)

    await callback.message.edit_text(text="Отправьте новую таблицу .xlsx")