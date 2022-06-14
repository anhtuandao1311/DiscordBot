from xml.etree.ElementInclude import LimitedRecursiveIncludeError
import discord
import random
from discord.ext import commands
from datetime import datetime

bot = commands.Bot(command_prefix = "`",help_command=None)

def is_me(ctx):
    pass


@bot.command()
async def ping(ctx):
    await ctx.send("Pong")


@bot.command()
async def coinflip(ctx):
    num = random.randint(1,2)
    if(num==1):
        await ctx.send("Head")
    else:
        await ctx.send("Tail")


@bot.command()
async def rps(ctx,hand):
    hands = ["✌️","✋","👊"]
    bothand = random.choice(hands)
    await ctx.send(bothand)
    if hand == bothand:
        await ctx.send("Draw")
    elif hand == "✌️":
        if bothand == "👊":
            await ctx.send("I won!")
        if bothand == "✋":
            await ctx.send("You won!")
    elif hand == "✋":
        if bothand == "👊":
            await ctx.send("You won!")
        if bothand == "✌️":
            await ctx.send("I won!")
    elif hand == "👊":
        if bothand == "✋":
            await ctx.send("I won!")
        if bothand == "✌️":
            await ctx.send("You won!")

@bot.command(aliases =["about"])
async def help(ctx):
    myembed=discord.Embed(title="Commands", description = "All available commmands for Brian", color = discord.Color.dark_purple())
    myembed.set_thumbnail(url = "https://www.kindpng.com/picc/m/118-1189293_brian-griffin-brian-family-guy-hd-png-download.png")
    myembed.add_field(name = "`ping",value = "Replies with Pong when you write `ping",inline=False)
    myembed.add_field(name = "`coinflip",value = "Replies with Head or Tail when you write `coinflip",inline=False)
    myembed.add_field(name = "`rps",value = "Play a game of Rock Paper Scissor with Brian when you write `rps",inline=False)
    await ctx.send(embed = myembed)

@bot.group()
async def edit(ctx):
    pass

@edit.command()
async def servername(ctx,*,input):          # *,input lay het input sau servername ke ca space
    await ctx.guild.edit(name = input)

@edit.command()
async def region(ctx,*,input):          
    await ctx.guild.edit(region = input)

@edit.command()
async def createtextchannel(ctx,*,input):          
    await ctx.guild.create_text_channel(name = input)

@edit.command()
async def createvoicechannel(ctx,*,input):          
    await ctx.guild.create_voice_channel(name = input)

@edit.command()
async def createrole(ctx,*,input):          
    await ctx.guild.create_role(name = input)

@bot.command()
async def kick(ctx,mem : discord.Member,*,reason=None):
    await ctx.guild.kick(mem,reason=reason)

@bot.command()
async def ban(ctx,mem : discord.Member,*,reason=None):
    await ctx.guild.ban(mem,reason=reason)

@bot.command()
async def unban(ctx,*,input):
    name,discriminator = input.split("#")
    banned = await ctx.guild.bans()
    for bannedmem in banned:
        username = bannedmem.user.name
        disc = bannedmem.user.discriminator
        if name == username and discriminator == disc:
            await ctx.guild.unban(bannedmem.user)
@bot.command()
async def purge(ctx,amount,day : int=None,month : int=None,year : int=datetime.now().year):
    if amount == "/":
        if day==None or month==None:
            return
        else:
            await ctx.channel.purge(after = datetime(year,month,day))
    else:
        await ctx.channel.purge(limit = int(amount)+1)      # cong 1 de xoa luon len `purge

@bot.command()
async def mute(ctx,mem : discord.Member):
    await mem.edit(mute=True)

@bot.command()
async def unmute(ctx,mem : discord.Member):
    await mem.edit(mute=False)

@bot.command()
async def deafen(ctx,mem : discord.Member):
    await mem.edit(deafen=True)

@bot.command()
async def undeafen(ctx,mem : discord.Member):
    await mem.edit(deafen=False)

@bot.command()
async def voicekick(ctx,mem : discord.Member):
    await mem.edit(voice_channel=None)


bot.run("OTg1NTY5MTM2MzYzMDQ4OTYy.GbRTwn.rosXmsb7OgD1iMCZ-QApPhTMExDI6VvLe1Qx1s")