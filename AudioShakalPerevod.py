from pydub import AudioSegment
from .. import loader, utils
import io
import os
def it("<b>Я(.fv) не поддерживаю аудио стоны! Только голосовые!</b>")
			os.remove(fname)
			return
		audio = audio + lvl
		m = io.BytesIO()
		m.name="voice.ogg"
		audio.export(m, format="ogg")
		await message.client.send_file(message.to_id, m, reply_to=reply.id, voice_note=True)
		await message.delete()
		os.remove(fname)

		
