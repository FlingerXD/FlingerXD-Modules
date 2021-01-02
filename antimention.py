from .. import loader, utils
from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest


@loader.tds
class AntiMentionMod(loader.Module):
    """Режим AntiMention."""
    strings = {'name': 'AntiMention'}

    async def client_ready(self, client, db):
        self.db = db

    async def antimentioncmd(self, message):
        """Включить/выключить режим AntiMention. Использование: .antimention <clearall* (по желанию)>.\n* - выключает режим во всех чатах."""
        am = self.db.get("AntiMention", "am", [])
        ac = self.db.get("AntiMention", "action", {})
        args = utils.get_args_raw(message)
        if args == "clearall":
            self.db.set("AntiMention", "am", [])
            self.db.set("AntiMention", "action", {})
            return await message.edit("<b>[AntiMention]</b> Режим выключен во всех чатах.")
        if not message.is_private:
            chat = await message.get_chat() 
            if not chat.admin_rights and not chat.creator:
                return await message.edit("<b>Я не админ здесь.</b>")
            else:
                if chat.admin_rights.delete_messages == False:
                    return await message.edit("<b>У меня нет нужных прав.</b>") 
            chatid = str(message.chat_id)
            if chatid in am:
                am.remove(chatid)
                ac.pop(chatid)
                self.db.set("AntiMention", "am", am)
                return await message.edit("<b>[AntiMention]</b> Деактивирован в этом чате.")

            am.append(chatid)
            ac.setdefault(chatid, {})
            ac[chatid].setdefault("action", "none")
            ac[chatid].setdefault("exceptions", [])
            self.db.set("AntiMention", "action", ac)
            self.db.set("AntiMention", "am", am)
            return await message.edit("<b>[AntiMention]</b> Активирован в этом чате.")
        else: return await message.edit("<b>[AntiMention]</b> Это не чат!")

    async def amexcmd(self, message):
        """Добавить исключения/посмотреть список исключений. Используй: .amex <@ или реплай> или <clear>."""
        if not message.is_private:
            am = self.db.get("AntiMention", "am", [])
            ac = self.db.get("AntiMention", "action", {})
            chatid = str(message.chat_id)
            args = utils.get_args_raw(message)
            reply = await message.get_reply_message()
            if chatid not in am: return await message.edit("<b>[AntiMention]</b> В этом чате режим деактивирован.")
            if "exceptions" not in ac[chatid]:
                ac[chatid].setdefault("exceptions", [])
            if not args and not reply:
                ls = ac[chatid]["exceptions"] 
                users = ""
                for _ in ls:
                    user = await message.client.get_entity(int(_))
                    users += f"• <a href=\"tg://user?id={int(_)}\">{user.first_name}</a> | <b>[</b><code>{_}</code><b>]</b>\n"
                return await message.edit(f"<b>Исключения в этом чате: {len(ls)}</b>\n\n{users}")
            if args == "clear":
                ac[chatid].pop("exceptions") 
                self.db.set("AntiMention", "action", ac)
                return await message.edit(f"<b>[AntiMention]</b> Список исключений в этом чате очищен.")
            try:
                if args: user = await message.client.get_entity(int(args) if args.isnumeric() else args)
                else: user = await message.client.get_entity(reply.sender_id)
            except ValueError: await message.edit("<b>Не удалось найти этого пользователя.</b>")
            userid = str(user.id)
            if userid not in ac[chatid]["exceptions"]:
                ac[chatid]["exceptions"].append(userid) 
                self.db.set("AntiMention", "action", ac)
                return await message.edit(f"<b>[AntiMention]</b> {user.first_name} добавлен в список исключений.")
            ac[chatid]["exceptions"].remove(userid) 
            self.db.set("AntiMention", "action", ac)
            return await message.edit(f"<b>[AntiMention]</b> {user.first_name} удалён из списка исключений.")
        else: return await message.edit("<b>[AntiMention]</b> Это не чат!")

    async def amstatuscmd(self, message):
        """Статус режима AntiMention."""
        if not message.is_private:
            am = self.db.get("AntiMention", "am", [])
            if str(message.chat_id) in am: return await message.edit("<b>[AntiMention - Status]</b> Активирован в этом чате.")
            else: return await message.edit("<b>[AntiMention - Status]</b> Деактивирован в этом чате.")
        else: return await message.edit("<b>[AntiMention]</b> Это не чат!")

    async def swamcmd(self, message):
        """Переключить режим AntiMention. Используй: .swam <режим>.\nДоступные режимы: kick/ban/none."""
        if not message.is_private:
            am = self.db.get("AntiMention", "am", [])
            ac = self.db.get("AntiMention", "action", {})
            args = utils.get_args_raw(message)
            chatid = str(message.chat_id)
            if chatid not in am: return await message.edit("<b>[AntiMention - Mode]</b> В этом чате режим деактивирован.")
            if args:
                if args == "kick":
                    ac[chatid].update({"action": "kick"})
                elif args == "ban":
                    ac[chatid].update({"action": "ban"})
                elif args == "none":
                    ac[chatid].update({"action": "none"})
                else: return await message.edit("<b>[AntiMention - Mode]</b> Такого режима нет в списке.\nДоступные режимы: kick/ban/none.")
                self.db.set("AntiMention", "action", ac)
                return await message.edit(f"<b>[AntiMention - Mode]</b> Теперь при упоминании в чате будет выполняться действие: {ac[chatid]['action']}.")
            else: return await message.edit(f"<b>[AntiMention - Mode]</b> При упоминании в чате будет выполняться действие: {ac[chatid]['action']}.")
        else: return await message.edit("<b>[AntiMention]</b> Это не чат!")


    async def watcher(self, message):
        """Продам модуль!!"""
        try:
            am = self.db.get("AntiMention", "am", [])
            ac = self.db.get("AntiMention", "action", {})
            chatid = str(message.chat_id)
            if chatid not in am: return
            if message.mentioned:
                userid = message.sender_id
                if str(userid) not in ac[chatid]["exceptions"]:
                    try:
                        if ac[chatid]["action"] == "kick":
                            await message.client.kick_participant(int(chatid), userid)
                        elif ac[chatid]["action"] == "ban":
                            await message.client(EditBannedRequest(int(chatid), userid, ChatBannedRights(until_date=None, view_messages=True)))
                        else: pass
                    except: pass 
                    await message.client.delete_messages(int(chatid), message.id)
        except: pass