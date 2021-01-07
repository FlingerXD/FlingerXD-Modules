import io
from .. import loader, utils
from random import randrange as r
from PIL import Image, ImageDraw

@loader.tds 
class HairMod(loader.Module):
    """Волос хаха!!"""
    strings = {'name': 'Hair'}

    async def haircmd(self, message):
        """Волос!"""
        reply = await message.get_reply_message()
        if not reply: return await message.edit("Нет реплая на картинку/стикер.")
        if reply.photo or reply.file.ext == ".webp":
            im = Image.open(io.BytesIO(await message.client.download_file(reply, bytes)))
            draw = ImageDraw.Draw(im)
            w, h = im.size
            x = r(w)
            y = r(h)
            b = r(300)
            c = r(550)
            a = r(350)
            draw.arc((x, y, x + b, y + c), a, 180 + a, fill="black", width=1)
            out = io.BytesIO()
            if reply.file.ext == ".webp":
                out.name = "witHair.webp"
            else:
                out.name = "witHair.png"
            im.save(out)
            out.seek(0) 
            await message.client.send_file(message.to_id, out, reply_to=reply.id if reply else None) 
            await message.delete()
        else: return await message.edit("Это не картинка/стикер.")