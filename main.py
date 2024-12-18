import disnake
from disnake.ext import commands
import os
bot = commands.Bot(command_prefix="!", help_command=None, intents=disnake.Intents.all())
token = 'MTMxMzQxNzIzNTcwODEyMTEyOA.GYIgUz.e_7aOJj371EheKeYhX_T-J0pCS7V8k2_-y1DnE'

@bot.event
async def on_ready():
    print('Бот включен.')
    await bot.change_presence(activity= disnake.Game(name="Call Of Dragons")) 

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

bot.run(token)