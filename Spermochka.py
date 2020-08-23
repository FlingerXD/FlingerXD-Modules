#by @FlinGer_Bs
from time import sleep
from telethon import events
import asyncio
from.. import loader 

def register(cb):
	cb(SpermaMod()) 
	
class SpermaMod(loader.Module):
	"""Сперма"""
	strings = {'name': 'Сперма'} 
	
	async def spermacmd(self, message):
		"""Просто .sperma"""
		for i in range(25):
			a = i + 1
			sleep(0.1)
			await message.edit("В вас запустили волшебной спермой! " + "💦💦💦👀💦💦💦☁💦💦💦💦💦💦👅💦💦💦💦💦💦💦💦💦💦💦Кинь эту сперму 7 друзьям и тебя будет ждать удача💦💦.💦эта сперма💦.💦счастья! " + "🎅👸обрызгай всех кого любишь!" +"Уиииииииии" * a + "...")

