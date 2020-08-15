# requires: pillow, pymorphy2
import logging
from .. import loader, utils
import telethon
import requests
from PIL import Image, ImageFont, ImageDraw 
import 
	draw = ImageDraw.Draw(canvas)

	draw.text((120, 5), 'ахах семья ' + caption_mlt, (0,0,0), font=ImageFont.truetype(io.BytesIO(font), 32))

	family = [
		{ 'name': 'мама алкашка', 'cords': (60, 100), 'size': 160 },
		{ 'name': 'папа лох', 'cords': (260, 80), 'size': 180 },
		{ 'name': 'нормальный сын', 'cords': (60, 380), 'size': 125 },
		{ 'name': 'лесби дочь', 'cords': (230, 320), 'size': 125 },
		{ 'name': 'шлюха дочь', 'cords': (225, 380), 'size': 125 },
		{ 'name': 'сын гей', 'cords': (340, 390), 'size': 125 },
	]

	for member in family:
		place(canvas, image, member['cords'], member['size'])

	for member in family:
		placeText(canvas, member['cords'], member['size'], member['name'] + ' ' + caption, font)


	temp = BytesIO()
	canvas.save(temp, format="png")
	return temp.getvalue()
	
async def check_media(message, reply):
	if reply and reply.media:
		if reply.photo:
			data = reply.photo
		elif reply.document:
			if reply.gif or reply.video or reply.audio or reply.voice:
				return None
			data = reply.media.document
		else:
			return None
	else:
		return None
	if not data or data is None:
		return None
	else:
		data = await 
