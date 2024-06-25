import disnake
from disnake.ext import commands

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents) # в '' вставляете свой префикс

bot.load_extensions('cogs') # загружаем все файлы с когами

@bot.event
async def on_ready():
	print('YT - JomixCode') # print это то что будет выводится в консоль
	print('Бот Активный')

@bot.command()
async def hello(ctx):
	member = ctx.author # создали переменую что member это ctx.author
	await ctx.reply(f'Привет {member.mention}!')

bot.run('token')
