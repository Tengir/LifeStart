from aiogram import Router, Bot
from aiogram.types import Message
from aiogram import F
from aiogram.utils.media_group import MediaGroupBuilder

from data import Data

router = Router()


@router.message(F.text.lower().in_(["дайджест", "digest"]))
async def digest(msg: Message, bot: Bot):
    data = Data()
    text = data.message.digest.text
    files_id = data.message.digest.files_id

    # Если нет фото.
    if len(files_id) == 0:
        await msg.answer(text)

    media_group = MediaGroupBuilder(caption=text)
    for file_id in files_id:
        media_group.add_photo(file_id)

    chat_id = msg.chat.id
    await bot.send_media_group(chat_id=chat_id, media=media_group.build())
