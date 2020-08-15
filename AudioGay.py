ioSegment.from_file(fname, "ogg")
		else:
			await message.edit("<b>Я(.fv) не поддерживаю аудио стоны(бывает)! Только голосовые!</b>")
			os.remove(fname)
			return
		audio = audio + lvl
		m = io.BytesIO()
		m.name="voice.ogg"
		audio.export(m, format="ogg")
		await message.client.send_file(message.to_id, m, reply_to=reply.id, voice_note=True)
		await message.delete()
		os.remove(fname)

		
