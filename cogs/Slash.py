# импортируем нужные библиотеки

import disnake
from disnake.ext import commands

# создаем новый класс

class Slash(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    # создаем слеш команду
    @commands.slash_command(name="embed", description="Отправить Embed", guild_ids=[123]) # в name вставляете название команды, в description вставляете описание команды, в guild_ids вставляете id сервера
    async def embed(self, interaction: disnake.AppCommandInteraction): # передаем параметры в функцию
        embed = disnake.Embed(title="Тайтл Embed'а", description="Описание Embed'a") # создаем embed
        await interaction.response.send_message(embed=embed) # отправляем embed

def setup(bot): # функция подключения кога (передаем бота)
    bot.add_cog(Slash(bot)) # добавляем ког