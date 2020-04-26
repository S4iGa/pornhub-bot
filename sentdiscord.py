import discord
import config
import porn
from datetime import datetime
from discord.ext import commands


tk = config.TOKEN
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('エロ動画見つけてきまっせ！')

@bot.command()
async def nuki(ctx, arg):
    videos = porn.getEroVideo(arg)
    i = 0
    for value in videos:
        if i == 3:
            break
        else:
            message = "・"+value.title+"\nURL:"+value.url
            await ctx.send(message)
            i += 1

bot.run(tk)
