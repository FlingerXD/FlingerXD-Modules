from .. import loader, utils

def register(cb):
    cb(FilesUploaderMod())
class FilesUploaderMod(loader.Module):
    strings = {'name': 'FilesUploader'}
    async def fupcmd(self, message):
        name = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        fname = f'{name or reply.file.name}'
        await message.client.download_media(reply, f'/var/www/html/files/{fname}')
        await message.edit(f'Файл был сохранён как: <code>{fname}</code>.\n\n'
                           f'Файл доступен тут: <code>https://flinger.ml/files/{fname}</code>.')