from pydub import AudioSegment

		audio.export(m, format="ogg")
		await message.client.send_file(message.to_id, m, reply_to=reply.id, voice_note=True)
		await message.delete()
		os.remove(fname)

		
