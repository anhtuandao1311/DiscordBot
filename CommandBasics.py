import asyncio
import discord
import os
import yt_dlp
import random
import glob
import os.path
from discord.ext import commands
from datetime import datetime
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "`",help_command=None,intents = intents)

def is_me(ctx):
    return ctx.author.id == 599076572745695233

def starts_with_a(msg):
    return msg.content.startswith("a") or msg.content.startswith("`purge")


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
@commands.has_role("🥉Bro")
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
@commands.check(is_me)
async def kick(ctx,mem : discord.Member,*,reason=None):
    await ctx.guild.kick(mem,reason=reason)

@bot.command()
@commands.check(is_me)
async def ban(ctx,mem : discord.Member,*,reason=None):
    await ctx.guild.ban(mem,reason=reason)

@bot.command()
@commands.check(is_me)
async def unban(ctx,*,input):
    name,discriminator = input.split("#")
    banned = await ctx.guild.bans()
    for bannedmem in banned:
        username = bannedmem.user.name
        disc = bannedmem.user.discriminator
        if name == username and discriminator == disc:
            await ctx.guild.unban(bannedmem.user)

@bot.command()
@commands.check(is_me)
async def purge(ctx,amount,day : int=None,month : int=None,year : int=datetime.now().year):
    if amount == "/":
        if day==None or month==None:
            return
        else:
            await ctx.channel.purge(after = datetime(year,month,day))
    else:
        await ctx.channel.purge(limit = int(amount)+1)      # cong 1 de xoa luon len `purge


@bot.command()
@commands.has_role("🥉Bro")
async def mute(ctx,mem : discord.Member):
    await mem.edit(mute=True)

@bot.command()
@commands.has_role("🥉Bro")
async def unmute(ctx,mem : discord.Member):
    await mem.edit(mute=False)

@bot.command()
@commands.has_role("🥉Bro")
async def deafen(ctx,mem : discord.Member):
    await mem.edit(deafen=True)

@bot.command()
@commands.has_role("🥉Bro")
async def undeafen(ctx,mem : discord.Member):
    await mem.edit(deafen=False)

@bot.command()
@commands.has_role("🥉Bro")
async def voicekick(ctx,mem : discord.Member):
    await mem.edit(voice_channel=None)

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

queuelist = []
filestodelete = []
titles = []
now_playing = ""

def is_connected(ctx):
    voice_client = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
    return voice_client and voice_client.is_connected()

@bot.command(aliases = ["p"])
async def play(ctx, *,searchword):
    if not is_connected(ctx):
        await ctx.author.voice.channel.connect()
    ydl_options = {}
    voice = ctx.voice_client
    # get title
    if searchword[0:4]=="http" or searchword[0:3]=="www":
        with yt_dlp.YoutubeDL(ydl_options) as ydl:
            info = ydl.extract_info(searchword,download = False)
            title = info["title"]
            url = searchword
            name = title
            if "/" in title:
                title = title.replace("/","")
    if searchword[0:4]!="http" and searchword[0:3]!="www":
        with yt_dlp.YoutubeDL(ydl_options) as ydl:
            info = ydl.extract_info(f"ytsearch:{searchword}",download = False)["entries"][0]
            title = info["title"]
            url = info["webpage_url"]
            name = title
            if "/" in title:
                title = title.replace("/","")

    ydl_options = {
        'format' : 'bestaudio/best',
        "outtmpl" : f"{title}.mp3",
        "postprocessors": 
        [{"key" : "FFmpegExtractAudio", "preferredcodec" : "mp3", "preferredquality" : "192"}]
        }


    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        ydl.download([url])

    folder_path = r'C:\Study\Discord Course'
    file_type = r'\*mp3'
    files = glob.glob(folder_path + file_type)
    max_file = max(files, key=os.path.getctime)
    filestodelete.append(max_file)

    if voice.is_playing():
        queuelist.append(max_file)
        titles.append(name)
        await ctx.send(f"Added ** {name} ** to Queue :musical_note:")
    else:
        voice.play(discord.FFmpegPCMAudio(f"{max_file}"),after = lambda e : check_queue())
        await ctx.send(f"Playing ** {name} ** :musical_note:")
        global now_playing 
        now_playing = name
        await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.listening,name = name))
    
    def check_queue():
        try:
            if queuelist[0]!=None:
                try:
                    voice.play(discord.FFmpegPCMAudio(f"{queuelist[0]}"),after = lambda e : check_queue())
                    global now_playing 
                    now_playing = titles[0]
                    coro = bot.change_presence(activity = discord.Activity(type = discord.ActivityType.listening,name = titles[0]))
                    fut = asyncio.run_coroutine_threadsafe(coro,bot.loop)
                    fut.result()
                    queuelist.pop(0)
                    titles.pop(0)
                except discord.errors.ClientException:
                    for file in filestodelete:
                        os.remove(f"{file}")
                    queuelist.clear()
                    titles.clear()
                    filestodelete.clear()
        except IndexError:
            for file in filestodelete:
                    os.remove(f"{file}")
            queuelist.clear()
            titles.clear()
            filestodelete.clear()
        
@bot.command()
async def pause(ctx):
    if ctx.voice_client.is_playing() == True:
        ctx.voice_client.pause()
    else:
        await ctx.send("I am not playing anything")

@bot.command(aliases = ["skip","s"])
async def stop(ctx):
    if ctx.voice_client.is_playing() == True:
        ctx.voice_client.stop()
    else:
        await ctx.send("I am not playing anything")

@bot.command()
async def resume(ctx):
    if ctx.voice_client.is_playing() == True:
        await ctx.send("I am playing audio")
    else:
        ctx.voice_client.resume()

@bot.command(aliases = ["q"])
async def queue(ctx):
    if len(titles)==0:
        await ctx.send("No song in Queue")
    else:
        myembed=discord.Embed(title="Music Queue :musical_note:", description = "All songs in Queue", color = discord.Color.dark_purple())
        myembed.set_thumbnail(url = "https://www.kindpng.com/picc/m/118-1189293_brian-griffin-brian-family-guy-hd-png-download.png")
        for i,song in enumerate(titles,start = 1):
            myembed.add_field(name = f"{i}. {song} ",value= "\u200b" ,inline=False)
        await ctx.send(embed = myembed)
    
@bot.command(aliases = ["np"])
async def nowplaying(ctx):
    await ctx.send(f"Now Playing:  ** {now_playing} ** :musical_note:")
           
    
# Error

@purge.error
async def errorhandler(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You have to enter a date or a number")
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("You can only enter number")


@voicekick.error
async def errorhandler(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You don't have the necessary role for this command")

@deafen.error
async def errorhandler(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You don't have the necessary role for this command")

@undeafen.error
async def errorhandler(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You don't have the necessary role for this command")

@mute.error
async def errorhandler(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You don't have the necessary role for this command")

@unmute.error
async def errorhandler(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You don't have the necessary role for this command")

@servername.error
async def errorhandler(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You don't have the necessary role for this command")

@bot.command
async def reload(ctx):
    bot.reload_extension("Cogs")

bot.load_extension("Cogs")
bot.run("OTg1NTY5MTM2MzYzMDQ4OTYy.GK_gXz.lQ3K7MLD6BmQhx_u4KEm326WeCKHJY3eFzrM4I")