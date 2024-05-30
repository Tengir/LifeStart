from aiogram import Router
from aiogram.types import Message
from aiogram import F

from config import CHANNEl, DIGEST_LIST
from utils.change_digest_dict import change_digest

router = Router()


def is_digest(post: Message): #, album: list[Message]) -> bool:
    # message.chat.id == CHANNEl and any(text.lower() in message.text.lower() for text in DIGEST_LIST)
    if post.chat.id != CHANNEl:
        return False
    if post.text is None and post.caption is None:
        return False
    if post.text is not None and not any(text.lower() in post.text.lower() for text in DIGEST_LIST):
        return False
    if post.caption is not None and not any(text.lower() in post.caption.lower() for text in DIGEST_LIST):
        return False
    return True


def get_files_id(album: list[Message]):
    if len(album) == 0:
        return []
    ans = []
    for msg in album:
        ans.append(msg.photo[-1].file_id)
    return ans

# Для теста указал айди своего канал.
# Тут не учтено, что может быть много хендлеров для каналов.
@router.channel_post()
async def channel_post(post: Message, album: list[Message]):
    if not is_digest(post):
        return
    files_id = get_files_id(album)
    if len(album) == 0:
        change_digest(post.text, files_id)
    else:
        change_digest(post.caption, files_id)
