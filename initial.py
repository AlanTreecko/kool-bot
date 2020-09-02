import discord
from discord.ext import commands
import requests
import sys
import random
import aiohttp
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageFilter
from io import BytesIO

bot = commands.Bot(command_prefix='+')
client = discord.Client()

# start up sequence

@bot.event
async def on_ready():
    print(bot.user.name)
    await bot.change_presence(activity=discord.Game(name='+help'))
    
# bot commands

@bot.command()
async def ping(ctx):
    """see if the bot is alive"""
    await ctx.send("Pong!")
    
@bot.command()
async def restart(ctx):
    """restart the bot"""
    sys.exit()
    
@bot.command()
async def schedule(ctx):
    """display the schedule"""
    channel=ctx.message.channel
    await ctx.send("Here is the schedule.")
    await channel.send(file=discord.File('images/schedule.png'))
    
@bot.command()
async def playing(ctx, *, arg):
    """change the bot's now playing"""
    await bot.change_presence(activity=discord.Game(name=arg))

@bot.command()
async def watching(ctx, *, arg):
    """change the bot's watching"""
    activity = discord.Activity(name=arg, type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)
    
@bot.command(pass_context=True)
async def rotate(ctx, *,  avamember : discord.Member=None):
    """rotate AVATARS"""
    userAvatarUrl = avamember.avatar_url # copy avatar URL to a smaller name
    response = requests.get(userAvatarUrl)
    img = Image.open(BytesIO(response.content)).convert('RGBA') # open image from URL and convert to a transparent RGB image
    rotated = img.rotate(random.randint(1, 360), expand=True) # rotate the image with a random range of 1 to 360 degrees
    rotated.save('rotated.png') # saves the rotated image
    channel=ctx.message.channel
    await channel.send(file=discord.File('rotated.png')) # sends image
    #BUG: WORKS WITH MENTIONS AND TAGS BUT NOT WITH ID!
    #BUG: CANNOT DETECT URLS THAT ARENT AVATARS!
    
    
    # Test Command for Failsafe
    
@bot.command()
async def failsafetest(ctx):
    """failsafe test"""
    msgatch = ctx.message.attachments[0]
    
    if msgatch.url == "":
        msgatch = avamember.avatar_url
    response = requests.get(msgatch.url)
    img2 = Image.open(BytesIO(response.content))
    result = img2.copy()
    result.save('imt.png') # saves the rotated image
    channel=ctx.message.channel
    await channel.send(file=discord.File('imt.png'))
    
@bot.command(pass_context=True)
async def giw(ctx, *,  avamember : discord.Member=None):
    """imports your avatar to the god i wish that were me meme"""
    userAvatarUrl = avamember.avatar_url # copy avatar URL to a smaller name
    response = requests.get(userAvatarUrl)
    font = ImageFont.truetype("arial.ttf", 24)
    img1 = Image.open("common/godiwish-base.png") # open base image
    img2 = Image.open(BytesIO(response.content)) # open avatar and resize to avatar size on base
    img2s = img2.resize((106, 106))
    back_img = img1.copy()
    back_img.paste(img2s, (9, 16))
    #draw = ImageDraw.Draw(back_img)
    #draw.text((175, 30), "alan", (0, 0, 0), font=font)
    back_img.save('back_img.png') # saves the rotated image
    channel=ctx.message.channel
    await channel.send(file=discord.File('back_img.png')) # sends image
    #BUG: WORKS WITH MENTIONS AND TAGS BUT NOT WITH ID!
    #BUG: CANNOT DETECT URLS THAT ARENT AVATARS!
    
@bot.command(pass_context=True)
async def imt(ctx, *,  avamember : discord.Member=None):
    """imports anthony onto a picture"""
    userAvatarUrl = avamember.avatar_url # copy avatar URL to a smaller name
    response = requests.get(userAvatarUrl)
    img1 = Image.open("common/imadethis-base.png") # open base image
    img2 = Image.open(BytesIO(response.content))#.convert('RGBA') # open avatar and resize to avatar size on base
    w, h = img1.size
    img2s = img2.resize((494, 461), resample=2)
    result = Image.new('RGBA', (494,461), (0, 0, 0, 0,))
    result.paste(img2s, (0,0))
    result.paste(img1, (0,0), mask=img1)
    result.save('imt.png') # saves the rotated image
    channel=ctx.message.channel
    await channel.send(file=discord.File('imt.png')) # sends image
    #BUG: WORKS WITH MENTIONS AND TAGS BUT NOT WITH ID!
    #BUG: CANNOT DETECT URLS THAT ARENT AVATARS!

@bot.command()
async def oso_chistoso(ctx):
    """oso chistoso"""
    channel=ctx.message.channel
    await channel.send(file=discord.File('images/funny_bear.png'))
    
    
# Error messages

        
bot.run('TOKEN')