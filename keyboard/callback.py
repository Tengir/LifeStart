from typing import Tuple

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


# Клавиатура для меню вызова теста.
call_menu_test = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="начать", callback_data="start_test")],
    [InlineKeyboardButton(text="назад", callback_data="menu")]
], resize_keyboard=True)


# Клавиатура для получения клавиатуры для ответов теста.
def get_inline_kb(buttons: list[Tuple]) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for button in buttons:
        text, callback = button
        kb.add(InlineKeyboardButton(text=text, callback_data=callback))
    return kb.as_markup()


# Клавиатура для админ панели, чтобы установить Дайджест.
admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="изменить FAQ", callback_data="set_faq"), InlineKeyboardButton(text="изменить таблицу", callback_data="set_table")]
], resize_keyboard=True)


