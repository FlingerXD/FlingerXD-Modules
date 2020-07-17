import io, random, glob, os
from PIL import Image
from telethon.tl.types import DocumentAttributeFilename
from uniborg.util import admin_cmd
"""Не подписался без матери остался"""
"""https://t.me/memeframe"""
"""автор этого говнокода @FlinGer_Bs, Помог @Nicolay230519 """


@borg.on(admin_cmd(pattern=".d(.*)", allow_sudo=True)) 
async def d(message):
	if message.is_reply:
		reply_message = await message.get_reply_message()
		data = await check_media(reply_message)
		if isinstance(data, bool):
			await message.edit("‮Reply to image, fucking idiot")
			return
	else:
		await message.edit("‮Reply to image, fucking idiot")
		return
"""await message.edit(" ‮`P` `r` `o` `c` `e` `s` `s` `i` `n` `g` `.` `.` `.`")
	await message.edit("`Е` `б` `ё` `м` `с` `я` `.` `.` `.`")"""
        for distorted in glob.glob("distorted*"):
		os.remove(distorted)
	for findistorted in glob.glob("*/distorted*"):
		os.remove(findistorted)

	fname = f"distorted{random.randint(1, 100)}.png"
	
	with open(fname, "wb") as file:
		file.write(await message.client.download_media(data, bytes))
	image = Image.open(fname)
	image.save(fname)
	imgdimens = image.width, image.height
	distortcmd = f"convert {fname} -liquid-rescale 60x60%! -resize {imgdimens[0]}x{imgdimens[1]}\! {fname}"
	os.system(distortcmd)
	image = Image.open(f"{fname}")
	buf = io.BytesIO()
	buf.name = 'image.png'
	image.save(buf, 'PNG')
	buf.seek(0)
"""await message.edit("‮`S` `e` `n` `d` `i` `n` `g` `.` `.` `.`")
	await message.edit("`К` `о` `н` `ч` `а` `е` `м` `.` `.` `.`")"""
        await message.client.send_file(message.chat_id, buf, reply_to=reply_message.id)
	await message.delete()
	

	
	
async def check_media(reply_message):
	if reply_message and reply_message.media:
		if reply_message.photo:
			data = reply_message.photo
		elif reply_message.document:
			if DocumentAttributeFilename(file_name='AnimatedSticker.tgs') in reply_message.media.document.attributes:
				return False
			if reply_message.gif or reply_message.video or reply_message.audio or reply_message.voice:
				return False
			data = reply_message.media.document
		else:
			return False
	else:
		return False

	if not data or data is None:
		return False
	else:
		return data

