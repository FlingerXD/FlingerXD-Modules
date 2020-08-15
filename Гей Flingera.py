import time
from .. import loader, utils

import logging


from telethon import types

logger = logging.attr(message.to_id, "user_id", None) == self._me.id:
            if self.get_afk() != False:
                afk_state = self.get_afk()
                ret = self.strings("afk_reason", message).format(afk_state)
                await utils.answer(message, ret)
            else:
                return

    def get_afk(self):
        return self._db.get(__name__, "afk", False)
