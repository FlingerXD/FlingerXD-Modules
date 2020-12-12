import io, requests
from .. import loader, utils
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter


def register(cb):
    cb(AskExitMod())

class AskExitMod(loader.Module):
    """Вы точно хотите покинуть чат?"""
    strings = {'name': 'Exit?'}

    async def exitcmd(self, message):
        """Используй .exit."""
        if message.chat:
            await message.delete()
            background = requests.get("https://fl1yd.ml/modules/stuff/exit.png").content
            font = requests.get("https://fl1yd.ml/modules/stuff/font4.ttf").content
            font = io.BytesIO(font)
            chat = await message.client.get_entity(message.to_id)
            text = f'Вы точно хотите покинуть {chat.title}?'
            font = ImageFont.truetype(font, 45)
            image = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
            draw = ImageDraw.Draw(image)
            w, h = draw.multiline_textsize(text=text, font=font)
            image = Image.open(io.BytesIO(background))
            x, y = image.size
            draw = ImageDraw.Draw(image)
            draw.multiline_text(((x - w) // 2, (y - h) // 1.9), text=text, font=font, fill="white", align="center")
            img1 = io.BytesIO()
            img1.name = "bg.png"
            image.save(img1, "png")
            img1.seek(0)

            img2 = io.BytesIO()
            await message.client.download_profile_photo(message.chat.id, img2)
            im = Image.open(img2)
            w, h = im.size
            img2 = Image.new("RGBA", (w, h), (0, 0, 0, 0))
            img2.paste(im, (0, 0))
            m = min(w, h)
            img2 = img2.crop(((w - m) // 2, (h - m) // 2, (w + m) // 2, (h + m) // 2))
            w, h = img2.size
            mask = Image.new('L', (w, h), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((10, 10, w - 10, h - 10), fill=255)
            mask = mask.filter(ImageFilter.GaussianBlur(2))
            img2 = ImageOps.fit(img2, (w, h))
            img2.putalpha(mask)
            im = io.BytesIO()
            im.name = "ava.webp"
            img2.save(im)
            im.seek(0)
            im1 = Image.open(img1)
            im2 = Image.open(im)
            im2 = im2.resize((190, 190))
            w1, h1 = im1.size
            im2.thumbnail((w1, h1))
            w2, h2 = im2.size
            x = (w1 - w2) // 2
            y = (h1 - h2) // 2
            im1.paste(im2, (x+3, y-130), im2)
            im1.save("output.webp")
            await message.client.send_file(message.to_id, 'output.webp')
        else: return await message.edit("Это не чат!")