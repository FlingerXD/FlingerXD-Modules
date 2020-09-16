from telethon import TelegramClient, events
from time import sleep
from random import choice

client = TelegramClient(...)
client.start()

@client.on(events.NewMessage(outgoing=True, pattern=r'.casino'))
async def casino(event):
	for i in range(1, 10):
		if i == 9:
			if choice([0, 0, 0, 0, 0, 0, 0, 0, 0, 1]):
				slot = choice(['🍒', '🎲', '💰', '💎', '💣', '🍎', '🐒', '🍌' ,'🌶', '🍋'])
				await event.edit('''⬛️⬛️⬛️⬛️⬛️
⬛️%s%s%s⬛️
⬛️⬛️⬛️⬛️⬛️''' % (slot, slot, slot))
			else:
				slot1 = choice(['🍒', '🎲', '💰', '💎', '💣', '🍎', '🐒', '🍌' ,'🌶', '🍋'])
				slot2 = choice(list(filter(lambda x: x != slot1, ['🍒', '🎲', '💰', '💎', '💣', '🍎', '🐒', '🍌' ,'🌶', '🍋'])))
				slot3 = choice(['🍒', '🎲', '💰', '💎', '💣', '🍎', '🐒', '🍌' ,'🌶', '🍋'])
		else:
			slot1 = choice(['🍒', '🎲', '💰', '💎', '💣', '🍎', '🐒', '🍌' ,'🌶', '🍋'])
			slot2 = choice(['🍒', '🎲', '💰', '💎', '💣', '🍎', '🐒', '🍌' ,'🌶', '🍋'])
			slot3 = choice(['🍒', '🎲', '💰', '💎', '💣', '🍎', '🐒', '🍌' ,'🌶', '🍋'])

			await event.edit('''⬛️⬛️⬛️⬛️⬛️
⬛️%s%s%s⬛️
⬛️⬛️⬛️⬛️⬛️''' % (slot1, slot2, slot3))
			sleep(0.5)

client.run_until_disconnected()
