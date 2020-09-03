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
    await bot.change_presence(activity=discord.Game(name='JESUS IS MY CO-PILOT AND WERE CRUSING FOR PUSSY!'))
    
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
    """display the morton schedule"""
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
async def dummy(ctx, *user : discord.Member):
    """DUMMY"""
    print("DUMMY TAG")
    print(user)
    print("FAILSAFETEST CALLED")
    img1 = await grabimage(ctx, * user)
    if img1 == None:
        await ctx.send("I'm sorry, I'm unable to find anything.")
    else:
        await ctx.send(img1)

async def grabimage(ctx, *user : discord.Member):
    print("FAILSAFETEST ACTIVATED")
    if len(ctx.message.attachments) == 1: # if there is atleast 1 attachment, then do this block
        attachment = ctx.message.attachments[0] # shorten name
        attachedurl = attachment.url # copy attachment URL to a smaller name
        response = requests.get(attachedurl) # get attachment url
        img1 = Image.open(BytesIO(response.content)).convert('RGBA') # open attachment from URL and convert to a RGBA image
        return img1 # return img1
    if len(ctx.message.mentions) == 1:
        mesmen = ctx.message.mentions # return list of who was mentioned in message
        user = mesmen[0] # pick the first user in the list
        userAvatarUrl = user.avatar_url # copy avatar URL to a smaller name
        response = requests.get(userAvatarUrl) # get avatar URL
        img1 = Image.open(BytesIO(response.content)).convert('RGBA') # open avatar from URL and convert to a RGBA image
        return img1
    else:
        user = ctx.message.author
        await ctx.send("Failsafetest result: Mention found. End.") # remove when grabimage is complete
        userAvatarUrl = user.avatar_url # copy avatar URL to a smaller name
        response = requests.get(userAvatarUrl) # get avatar URL
        img1 = Image.open(BytesIO(response.content)).convert('RGBA') # open avatar from URL and convert to a RGBA image
        return img1 # return img1
    
@bot.command(pass_context=True)
async def rotate(ctx, *,  avamember : discord.Member=None):
    """rotates images by a random amount"""
    img1 = await grabimage(ctx)
    rotated = img1.rotate(random.randint(1, 360), expand=True) # rotate the image with a random range of 1 to 360 degrees
    rotated.save('tmp/rotate.png') # saves the rotated image
    channel=ctx.message.channel
    await channel.send(file=discord.File('tmp/rotate.png')) # sends image
    
@bot.command(pass_context=True)
async def giw(ctx, * user : discord.Member):
    """imports images to the god i wish that were me meme"""
    img1 = await grabimage(ctx)
    img2 = Image.open("common/godiwish-base.png").convert('RGBA') # open base image
    img1s = img1.resize((106, 106))
    giw = img2.copy()
    giw.paste(img1s, (9, 16))
    #draw = ImageDraw.Draw(back_img)
    #draw.text((175, 30), "alan", (0, 0, 0), font=font)
    giw.save('tmp/giw.png') # saves the rotated image
    channel=ctx.message.channel
    await channel.send(file=discord.File('tmp/giw.png')) # sends image
    
@bot.command(pass_context=True)
async def imt(ctx, *,  avamember : discord.Member=None):
    """imports anthony onto an image"""
    img1 = await grabimage(ctx)
    img2 = Image.open("common/imadethis-base.png") # open base image
    w, h = img2.size
    img1s = img1.resize((494, 461), resample=2)
    result = Image.new('RGBA', (494,461), (0, 0, 0, 0,))
    result.paste(img1s, (0,0))
    result.paste(img2, (0,0), mask=img2)
    result.save('tmp/imt.png') # saves the rotated image
    channel=ctx.message.channel
    await channel.send(file=discord.File('tmp/imt.png')) # sends image

@bot.command(pass_context=True)
async def aimd(ctx, *,  avamember : discord.Member=None):
    """ INCOMPLETE """
    userAvatarUrl = avamember.avatar_url # copy avatar URL to a smaller name
    response = requests.get(userAvatarUrl)
    img = Image.open(BytesIO(response.content))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("common/comicsans.ttf", 24)
    w, h = img.size
    draw.text((w / 2 , h / 2), "made by anthony ibarra", (0, 0, 0), font=font)
    img.save('aimd.png') # saves the rotated image
    channel=ctx.message.channel
    await channel.send(file=discord.File('aimd.png')) # sends image

@bot.command()
async def oso_chistoso(ctx):
    """oso chistoso"""
    channel=ctx.message.channel
    await channel.send(file=discord.File('images/funny_bear.png'))
    
    
# Error messages

        
bot.run('TOKEN')
