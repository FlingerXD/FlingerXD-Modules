# -*- coding: utf-8 -*-

#   Friendly Telegram (telegram userbot)
#   Copyright (C) 2018-2020 @DneZyeK | sub to @KeyZenD

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.

#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging
from .. import loader, utils
import telethon
from requests import post

logger = logging.getLogger(__name__)

async def register(cb):
	cb(WhoIsMod())


@loader.tds
class GGdotGGMod(loader.Module):
	"""Сокращение ссылок через сервис gg.gg"""
	strings = {
		"name": "gg.gg",
		"some_rong": "<b>Ты делаешь что-то не так!\nНапиши</b> <code>.help gg.gg</code> <b>для информации.</b>"
	}
	
	async def client_ready(self, client, db):
		self.client = client
		
	async def ggcmd
			long_url = m_text
				
		
			await utils.answer(message, check)
			return
		await utils.answer(message, "Create...")
		short = post('http://gg.gg/create', data={'custom_path': None, 'use_norefs': '0', 'long_url': long_url, 'app': 'site', 'version': '0.1'}).text
		await utils.answer(message, short)

