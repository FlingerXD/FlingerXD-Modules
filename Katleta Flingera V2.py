from telethon import events
from .. import loader, utils
import os
import requests
from PIL import Image,ImageFont,ImageDraw 
import re
import io
from textwrap import wrap

def register(cb):
	cb(JacquesTwoMod())
	
class JacquesTwoMod(loader.Module):
	"""Жаконизатор V2"""
	strings = {
		'name': 'Катлета Флингера V2',
		'usage': 'ТАК СЛОЖНО НАПИСАТЬ <code>(Ты еблан).help Жаконизатор V2</code> , ДОЛБАЕБ?',
	}
	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []
	async def client_ready(self, client, db):
		self._db = db
		self._client = client
		self.me = await client.get_me()
		
	async def j2cmd(self, message):
		""".j <реплай на сообщение/свой текст>\n@cheats_and_modulesFTG канал автора :3"""
		
		ufr = requests.get("http://allfont.de/cache/fonts/lobster_0bb8e965b43150fe5f875de8f9692762.ttf")
		f = ufr.content
		
		reply = await message.get_reply_message()
		args = utils.get_args_raw(message)
		if not args:
			if not reply:
				await utils.answer(message, self.strings('usage', message))
				return
			else:
				txt = reply.raw_text
		else:
			txt = utils.get_args_raw(message)
		await message.edit("<b>Я сосал(а) Жаку Фреско ...</b>")
		pic = requests.get("https://0x0.st/i6bd.jpg")
		pic.raw.decode_content = True
		img = Image.open(io.BytesIO(pic.content)).convert("RGB")
 
		W, H = img.size
		#txt = txt.replace("\n", "𓃐")
		text = "\n".join(wrap(txt, 20))
		t = text + "\n"
		#t = t.replace("𓃐","\n")
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype(io.BytesIO(f), 35, encoding='UTF-8')
		w, h = draw.multiline_textsize(t, font=font)
		imtext = Image.new("RGBA", (w+50, h+50), (0, 0,0,0))
		draw = ImageDraw.Draw(imtext)
		draw.multiline_text((40, 40),t,(225,225,225),font=font, align='left')
		imtext.thumbnail((450, 330))
		w, h = 450, 330
		img.paste(imtext, (2,100), imtext)
		out = io.BytesIO()
		out.name = "@sad0ff.jpg"
		img.save(out)
		out.seek(0)
		await message.client.send_file(message.to_id, out, reply_to=reply)
		await message.delete()
