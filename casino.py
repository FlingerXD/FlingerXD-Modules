from.. import loader 
from time import sleep
from random import choice


def register(cb):
    cb(CasinoMod()) 
    
class CasinoMod(loader.Module):
    """Casino""" 
    strings = {'name': 'Casino'} 
    
    async def casinocmd(self, event):
        """Casino da"""
        for i in range(1, 10):
            if i == 9:
                if choice([0, 0, 0, 0, 0, 0, 0, 0, 0, 1]):
                    slot = choice(['🍒', '🎲', '💰', '💎', '💣', '🍎', '🐒', '🍌' ,'🌶', '🍋'])
                    await event.edit('''⬛️⬛️⬛️⬛️⬛️
⬛️%s%s%s⬛️
⬛️⬛️⬛️⬛️⬛️''' % (slot, slot, slot))
                else:
                    slot1 = choice(['🍒', '🎲', '💰', '💎', '💣', '🍎', '🐒', '🍌' ,'🌶', '🍋'])
                    slot2 = choice(list(filter(lambda x: x != slot1, ['🍒', '🎲', '💰', '💎', '💣', '🍎', '🐒', '🍌' ,'🌶', '🍋'])))
                    slot3 = choice(['🍒', '🎲', '💰', '💎', '💣', '🍎', '🐒', '🍌' ,'🌶', '🍋'])
            else:
                slot1 = choice(['🍒', '🎲', '💰', '💎', '💣', '🍎', '🐒', '🍌' ,'🌶', '🍋'])
                slot2 = choice(['🍒', '🎲', '💰', '💎', '💣', '🍎', '🐒', '🍌' ,'🌶', '🍋'])
                slot3 = choice(['🍒', '🎲', '💰', '💎', '💣', '🍎', '🐒', '🍌' ,'🌶', '🍋'])

                await event.edit('''⬛️⬛️⬛️⬛️⬛️
⬛️%s%s%s⬛️
⬛️⬛️⬛️⬛️⬛️''' % (slot1, slot2, slot3))
                sleep(0.5) 