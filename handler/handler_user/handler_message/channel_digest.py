from aiogram import Router
from aiogram.types import Message
from aiogram import F


from config import CHANNEl
from utils.change_digest_dict import change_digest

router = Router()


# Для теста указал айди своего канал.
@router.channel_post(
    F.sender_chat.id == -1002082046843 and
    F.text.lower().contains('#дайджест'))  # TODO  айди заменить на CHANNEL.
async def channel_post(post: Message):
    change_digest(post.text)
