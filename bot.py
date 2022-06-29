from image_generation import *
import discord
from discord.ext import commands
from config import settings
from io import BytesIO
import io
from PIL import Image

img_gen = Image_generation(790, settings['wkhtmltoimage_path'])

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.event
async def on_ready():
    print('Авторизирован как {0.user}'.format(bot))

@bot.command()
async def new(ctx):
    if ctx.message.reference and (msg := ctx.message.reference.resolved) and isinstance(msg, discord.Message):
        channel = bot.get_channel(settings['quote_channel_id'])
        guild = await bot.fetch_guild(msg.guild.id)
        member = await guild.fetch_member(msg.author.id)
        top_role = member.roles[-1].color
        img_bytes = img_gen.generate(str(member.display_name), msg.content, msg.created_at.strftime("%d.%m.%Y"), f"rgb({top_role.r}, {top_role.g}, {top_role.b})", await member.avatar_url.read())
        image_file = discord.File(io.BytesIO(img_bytes),filename=f"quote.png")
        await channel.send(file=image_file)
    else:
        await ctx.send("Необходимо ответить на сообщение для цитирования!")

@bot.command()
async def fake(ctx, member: discord.Member, *args):
    if len(args) != 2:
        await ctx.send("Неверные аргументы команды! Шаблон: fake @user time \"text\"")
    else:
        channel = bot.get_channel(settings['quote_channel_id'])
        top_role = member.roles[-1].color
        img_bytes = img_gen.generate(str(member.display_name), args[1], args[0], f"rgb({top_role.r}, {top_role.g}, {top_role.b})", await member.avatar_url.read())
        image_file = discord.File(io.BytesIO(img_bytes),filename=f"quote.png")
        await channel.send(file=image_file)

bot.run(settings['token'])
#
#   
