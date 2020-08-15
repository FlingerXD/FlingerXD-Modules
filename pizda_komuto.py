from .. import loader, utils
from asyncio import sleep
import random


def register(cb):
    cb(KickRandomMod())


class KickRandomMod(loader.Module):
    """Пизда кому-то"""
    stringskick_participant(event.chat_id, user.id)
            await sleep(0.5)
        except:
            await event.edit('<b>Я лох, у меня нет прав чтобы кикнуть это чмо</b>')
            return

        # Кто кикнут.
        name = str(user.first_name)
        name += " " + user.last_name if user.last_name else ''
        await event.edit(
            f"Бог модуля Флингер пизданул <a href=\"tg://user?id={user.id}\">{user.first_name}</a>, и он улетел нахуй!")
