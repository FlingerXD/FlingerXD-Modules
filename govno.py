#by @FlinGer_Bs
from time import sleep
from telethon import events
import asyncio
from.. import loader 

def register(cb):
	cb(GovnoMod()) 
	
class GovnoMod(loader.Module):
	"""Говно"""
	strings = {'name': 'Govno'} 
	
	async def govnocmd(self, message):
		"""Просто .govno"""
		for i in range(25):
			a = i + 1
			sleep(0.1)
			await message.edit("Рот " + "в " + "говне " +"💩" * a + "...")


