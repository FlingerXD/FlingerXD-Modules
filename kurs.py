from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from .. import loader, utils

def register(cb):
    cb(KursMod())

class KursMod(loader.Module):
    """Курс валют by @exchange_rates_vsk_bot"""
    strings = {'name': 'Курс Валют'}

    async def kurscmd(self, event):
        """Используй: .kurs <число + инициалы валюты>."""
        chat = "@exchange_rates_vsk_bot"
        args = utils.get_args_raw(event)
        if not args:
            await event.edit("<b>Нет аргументов.</b>")
            return
        async with event.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True, from_users=1210425892))
                await event.client.send_message(chat, args)
                response = await response
            except YouBlockedUserError:
                await event.edit("<b>Разблокируй @exchange_rates_vsk_bot.</b>")
                return
            await event.edit(response.text)

    async def btccmd(self, event):
        """Курс биткоина в долларах"""
        await event.delete()
        await event.respond((await event.client.get_messages("bitcoin_kurs"))[0])