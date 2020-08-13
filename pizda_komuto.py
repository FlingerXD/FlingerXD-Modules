from .. import loader
from asyncio import sleep
import random


def register(cb):
	cb(KickRandomMod())

class KickRandomMod(loader.Module):
	"""Пизда кому-то"""
	strings = {'name': 'PizdaKomuto'}

	async def kickpizdacmd(self, event):
		"""Используй .kickpizda, чтобы пиздануть случайное существо (может кикнуть тебя)."""
		user = random.choice([i for i in await event.client.get_participants(event.to_id)])

		await event.edit('<b>Кто сейчас пизданется...</b>')
                #ti = await event.client.get_me()
                #await event.edit(ti)
		await sleep(3)

		# Попытка кика...
		try:
			#await event.client.kick_participant(event.chat_id, user.id)
			await sleep(0.5)
		except:
			await event.edit('<b>Я лох, у меня нет прав чтобы кикнуть это чмо</b>')
			return

		# Кто кикнут.
		name = str(user.first_name)
		name += " "+user.last_name if user.last_name else ''
		#await event.edit(f"Бог модуля Флингер пизданул <a href=\"tg://user?id={user.id}\">{user.first_name}</a>, и он улетел нахуй!")
                #ti = await event.client.get_me()
                #await event.edit(ti)
