from aiogram import Router
from aiogram import F
from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboard.callback import get_inline_kb
import keyboard.reply
from data import Data
from state import UserState

router = Router()


# Если нажата кнопка Начать тест и Юзер НЕ проходит тест.
@router.callback_query(
    F.data == "start_test",  ~StateFilter(UserState.test))
async def start_test(callback: CallbackQuery, state: FSMContext):
    await state.set_state(UserState.test)
    #  Сохраняем сообщения с тестом, чтобы при перезапуске удалить его.
    await state.update_data(q_num=0,
                            test_message=callback)
    text, answers = Data().question[0]
    await callback.message.edit_text(text=text,
                                     reply_markup=get_inline_kb(answers))


# Если нажата кнопка Начать тест и Юзер проходит уже тест.
# Удаляем предыдущий тест и начинаем заново.
@router.callback_query(
    F.data == "start_test", StateFilter(UserState.test))
async def already_start_test(callback: CallbackQuery, state: FSMContext):
    data: dict = await state.get_data()
    await data["test_message"].message.delete()
    await state.clear()
    await start_test(callback, state)

