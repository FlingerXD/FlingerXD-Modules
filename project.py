from .. import loader
from asyncio import sleep 

def register(cb):
	cb(SnowMod()) 
	
class SnowMod(loader.Module):
	"""Снег"""
	strings = {'name': 'Snow'}
        
	async def snowcmd(self, message):
		"""Используй .snow"""
		await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n\n\n\n\n\n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️')
		await sleep(0.75)
		await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n    ❄️    ❄️     ❄️     ❄️     ❄️   ❄️\n\n\n\n\n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️')
		await sleep(0.75)
		await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n    ❄️    ❄️     ❄️     ❄️     ❄️   ❄️\n❄️    ❄️    ❄️    ❄️    ❄️    ❄️       \n\n\n\n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️')
		await sleep(0.75)
		await message.edit(' ☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n   ❄️    ❄️     ❄️     ❄️     ❄️   ❄️\n❄️    ❄️    ❄️    ❄️    ❄️    ❄️       \n    ❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n\n\n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️')
		await sleep(0.75)
		await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n    ❄️    ❄️     ❄️     ❄️     ❄️   ❄️\n❄️    ❄️    ❄️    ❄️    ❄️    ❄️       \n    ❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n\n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️')
		await sleep(0.75)
		await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n    ❄️    ❄️     ❄️     ❄️     ❄️   ❄️\n❄️    ❄️    ❄️    ❄️    ❄️    ❄️       \n    ❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n  ❄️      ❄️    ❄️  ❄️      ❄️  ❄️ \n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️') 
		await sleep(1.25)
		await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n\n❄️    ❄️    ❄️    ❄️    ❄️    ❄️       \n    ❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n  ❄️      ❄️    ❄️  ❄️      ❄️  ❄️  \n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️')
		await sleep(0.75)
		await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n\n\n    ❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n  ❄️      ❄️    ❄️  ❄️      ❄️  ❄️ \n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️')
		await sleep(0.75)
		await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n\n\n\n❄️    ❄️    ❄️    ❄️    ❄️    ❄️     \n  ❄️      ❄️    ❄️  ❄️      ❄️  ❄️ \n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️')
		await sleep(0.75)
		await message.edit('☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁️\n\n\n\n\n  ❄️      ❄️    ❄️  ❄️      ❄️  ❄️ \n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️') 