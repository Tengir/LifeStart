from aiogram.fsm.state import State, StatesGroup


class UserState(StatesGroup):
    test = State()


class AdminState(StatesGroup):
    set_faq = State()
    set_table = State()
