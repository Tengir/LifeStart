from aiogram import Router, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import F
import pandas as pd
import os

from config import ADMINS
from database.sport_table import SportTable

from state import AdminState

from utils.change_faq import change_faq

router = Router()


@router.message(F.from_user.id.in_(ADMINS), StateFilter(AdminState.set_table),
                F.document)
async def set_table(msg: Message, state: FSMContext, bot: Bot):
    await state.clear()
    current_file = __file__
    path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(current_file))))

    print(path)
    await bot.download(
        msg.document,
        destination=f"{path}\\{msg.document.file_id}.xlsx"
    )
    data = read_excel_data(f"{path}\\{msg.document.file_id}.xlsx")
    SportTable().insert_data(data)

    await msg.answer(f"Готово")


def read_excel_data(file_name):
    try:
        data = pd.read_excel(file_name)
        data_list = data.values.tolist()
        print(data_list)
        return data_list
    except Exception as e:
        print(f"Error reading Excel file: {e}")
