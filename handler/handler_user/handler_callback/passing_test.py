from aiogram import Router
from aiogram import F
from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboard.callback import get_inline_kb
from data import Data
from state import UserState

from utils.generate_result_test import generate_result_test

router = Router()


# @router.callback_query(F.data == "start_test" and not StateFilter(UserState.test))
# async def start_test(callback: CallbackQuery, state: FSMContext):
#     await state.set_state(UserState.test)
#     await state.update_data(q_num=0)
#     text, answers = Data().question[0]
#     await callback.message.edit_text(text=text, reply_markup=get_inline_kb(answers))

# Заходим если мы проходим тест и НЕ начинаем тест снова.
@router.callback_query(StateFilter(UserState.test), F.data != "start_test")
async def passing_test(callback: CallbackQuery, state: FSMContext):
    data: dict = await state.get_data()

    # Ответы пользователя. Если их нет (тест только начался), то пустой список.
    user_answers = data.setdefault("user_answers", [])
    user_answers.append(int(callback.data))

    q_num = data["q_num"] + 1  # Номер следующего вопроса.
    await state.update_data(q_num=q_num, user_answers=user_answers)
    try:
        text, answers = Data().question[q_num]
        await callback.message.edit_text(text=text,
                                         reply_markup=get_inline_kb(answers))
    except IndexError:
        # Если вопросы в data_message закончились.
        answer_user = data["user_answers"]
        await state.clear()
        await callback.message.edit_text(generate_result_test(answer_user))
