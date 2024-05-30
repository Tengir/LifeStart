from handler.handler_user.handler_message.menu_message import router as r1
from handler.handler_user.handler_message.digest import router as r2
from handler.handler_user.handler_message.sections import router as r3
from handler.handler_user.handler_message.faq import router as r4
from handler.handler_user.handler_message.call_menu_test import router as r5
from handler.handler_user.handler_message.other import router as r6

from handler.handler_user.handler_callback.menu_callback import router as r7
from handler.handler_user.handler_callback.passing_test import router as r8
from handler.handler_user.handler_callback.start_test import router as r9

from handler.handler_user.handler_message.channel_digest import router as r10

routers = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10]
