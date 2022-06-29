from discord.ext import commands
import discord, yt_dlp, os, asyncio
import glob
import os.path
queuelist = []
filestodelete = []
titles = []
now_playing = ""
class MusicCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def join(self,ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    @commands.command()
    async def leave(self,ctx):
        await ctx.voice_client.disconnect()

    queuelist = []
    filestodelete = []
    titles = []
    now_playing = ""

    def is_connected(self,ctx):
        voice_client = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
        return voice_client and voice_client.is_connected()

    @commands.command(aliases = ["p"])
    async def play(self,ctx, *,searchword):
        if not self.is_connected(ctx):
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
            await self.bot.change_presence(activity = discord.Activity(type = discord.ActivityType.listening,name = name))
        
        def check_queue():
            try:
                if queuelist[0]!=None:
                    try:
                        voice.play(discord.FFmpegPCMAudio(f"{queuelist[0]}"),after = lambda e : check_queue())
                        global now_playing 
                        now_playing = titles[0]
                        coro = self.bot.change_presence(activity = discord.Activity(type = discord.ActivityType.listening,name = titles[0]))
                        fut = asyncio.run_coroutine_threadsafe(coro,self.bot.loop)
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

    @commands.command(aliases = ["skip","s"])
    async def stop(self,ctx):
        if ctx.voice_client.is_playing() == True:
            await ctx.send(f"Skipped ** {now_playing} ** :musical_note:")
            ctx.voice_client.stop()
        else:
            await ctx.send("I am not playing anything")

    @commands.command(aliases = ["q"])
    async def queue(self,ctx):
        if len(titles)==0:
            await ctx.send("No song in Queue")
        else:
            myembed=discord.Embed(title="Music Queue :musical_note:", description = "All songs in Queue", color = discord.Color.dark_purple())
            myembed.set_thumbnail(url = "https://www.kindpng.com/picc/m/118-1189293_brian-griffin-brian-family-guy-hd-png-download.png")
            for i,song in enumerate(titles,start = 1):
                myembed.add_field(name = f"{i}. {song} ",value= "\u200b" ,inline=False)
            await ctx.send(embed = myembed)
        
    @commands.command(aliases = ["np"])
    async def nowplaying(self,ctx):
        if ctx.voice_client.is_playing() == True:
            await ctx.send(f"Now Playing ** {now_playing} ** :musical_note:")
        else:
            await ctx.send("I am not playing anything")


    #Error



    @join.error
    async def errorhandler(self,ctx, error):
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send("You have to be connected to a Voice Channel.")

    @leave.error
    async def errorhandler(self,ctx, error):
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send("I am not in a Voice Channel.")

    @play.error
    async def errorhandler(self,ctx, error):
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send("You have to be connected to a Voice Channel.")

    @stop.error
    async def errorhandler(self,ctx, error):
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send("I am not in a Voice Channel.")

def setup(bot):
    bot.add_cog(MusicCog(bot))