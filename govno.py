#by @FlinGer_Bs
from time import sleep
from telethon import events
import asyncio
from.. import loader 

def register(cb):
	cb(GovnoMod()) 
	
class GovnoMod(
