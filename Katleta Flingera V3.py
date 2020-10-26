from telethon import events
from .. import loader, utils
import os
import requests
from PIL import Image,ImageFont,ImageDraw 
import re
import io
from textwrap import wrap

def register(cb):
	cb(JacquesThreeMod())
	
class JacquesThreeMod(loader.Module):
	"""Жаконизатор V3"""
	strings = {
		'name': 'Катлета Флингера V3',
		'usage': 'ТАК СЛОЖНО НАПИСАТЬ <code>(Ты еблан).help Жаконизатор V3</code> , ты пидарас или пидофил?',
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
		""".j3 <реплай на сообщение/свой текст>\n@TermuxTools_Hacking канал автора :3"""
		
		ufr = requests.get("https://github.com/Fl1yd/FTG-modules/blob/master/stuff/font2.ttf?raw=true")
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
		await message.edit("<b>На размышление дается 30 секунд...</b>")
		pic = requests.get("https://x0.at/lU0.jpg")
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
