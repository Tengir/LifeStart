from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Клавиатура для меню.
menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Тест"), KeyboardButton(text="Секции")],
    [KeyboardButton(text="Дайджест"), KeyboardButton(text="FAQ")]
], resize_keyboard=True, one_time_keyboard=False)


# Клавиатура для корусов с секциями. Не нужна. Оставлена на всякий случай.
# sections = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text="Корпус 1")],
#     [KeyboardButton(text="Корпус 2")],
#     [KeyboardButton(text="Корпус 3")],
#     [KeyboardButton(text="Назад в меню")]
# ], resize_keyboard=True)
