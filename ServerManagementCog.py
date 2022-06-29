from discord.ext import commands
import discord
from datetime import datetime
import random

class ServerManagementCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("BOT IS ONLINE")

    @commands.command()
    async def role(self,ctx):
        new_msg = await ctx.channel.send("Lord - 🍇\nBro - 🍓\nDJ - 🍈\nChecker - 🍆\nMemes-dealer - 🥥")
        await new_msg.add_reaction("🍇")
        await new_msg.add_reaction("🍓")
        await new_msg.add_reaction("🍈")
        await new_msg.add_reaction("🍆")
        await new_msg.add_reaction("🥥")

    @commands.Cog.listener()
    async def on_member_join(self,member):
        guild = member.guild
        guildname = guild.name
        dmchannel = await member.create_dm()
        await dmchannel.send("Welcome to {guildname}!")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
        emoji = payload.emoji.name
        member = payload.member
        messageid = payload.message_id
        guildid = payload.guild_id
        guild = self.bot.get_guild(guildid)
        channelid = payload.channel_id
        channel = self.bot.get_channel(channelid)
        msgobj = await channel.fetch_message(messageid)
        author = msgobj.author
        if emoji == "🍇" and author == self.bot.user and msgobj.content == "Lord - 🍇\nBro - 🍓\nDJ - 🍈\nChecker - 🍆\nMemes-dealer - 🥥":
            role = discord.utils.get(guild.roles,name = "💸Lord")
            await member.add_roles(role)
        if emoji == "🍓" and author == self.bot.user and msgobj.content == "Lord - 🍇\nBro - 🍓\nDJ - 🍈\nChecker - 🍆\nMemes-dealer - 🥥":
            role = discord.utils.get(guild.roles,name = "🥉Bro")
            await member.add_roles(role)
        if emoji == "🍈" and author == self.bot.user and msgobj.content == "Lord - 🍇\nBro - 🍓\nDJ - 🍈\nChecker - 🍆\nMemes-dealer - 🥥":
            role = discord.utils.get(guild.roles,name = "🎧Disc Jockey🎸")
            await member.add_roles(role)
        if emoji == "🍆" and author == self.bot.user and msgobj.content == "Lord - 🍇\nBro - 🍓\nDJ - 🍈\nChecker - 🍆\nMemes-dealer - 🥥":
            role = discord.utils.get(guild.roles,name = "😁Checker")
            await member.add_roles(role)
        if emoji == "🥥" and author == self.bot.user and msgobj.content == "Lord - 🍇\nBro - 🍓\nDJ - 🍈\nChecker - 🍆\nMemes-dealer - 🥥":
            role = discord.utils.get(guild.roles,name = "🎭Memes-dealer🧬")
            await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,payload):
        userid = payload.user_id
        emoji = payload.emoji.name
        messageid = payload.message_id
        guildid = payload.guild_id
        guild = self.bot.get_guild(guildid)
        member = guild.get_member(userid)
        channelid = payload.channel_id
        channel = self.bot.get_channel(channelid)
        msgobj = await channel.fetch_message(messageid)
        author = msgobj.author
        if emoji == "🍇" and author == self.bot.user and msgobj.content == "Lord - 🍇\nBro - 🍓\nDJ - 🍈\nChecker - 🍆\nMemes-dealer - 🥥":
            role = discord.utils.get(guild.roles,name = "💸Lord")
            await member.remove_roles(role)
        if emoji == "🍓" and author == self.bot.user and msgobj.content == "Lord - 🍇\nBro - 🍓\nDJ - 🍈\nChecker - 🍆\nMemes-dealer - 🥥":
            role = discord.utils.get(guild.roles,name = "🥉Bro")
            await member.remove_roles(role)
        if emoji == "🍈" and author == self.bot.user and msgobj.content == "Lord - 🍇\nBro - 🍓\nDJ - 🍈\nChecker - 🍆\nMemes-dealer - 🥥":
            role = discord.utils.get(guild.roles,name = "🎧Disc Jockey🎸")
            await member.remove_roles(role)
        if emoji == "🍆" and author == self.bot.user and msgobj.content == "Lord - 🍇\nBro - 🍓\nDJ - 🍈\nChecker - 🍆\nMemes-dealer - 🥥":
            role = discord.utils.get(guild.roles,name = "😁Checker")
            await member.remove_roles(role)
        if emoji == "🥥" and author == self.bot.user and msgobj.content == "Lord - 🍇\nBro - 🍓\nDJ - 🍈\nChecker - 🍆\nMemes-dealer - 🥥":
            role = discord.utils.get(guild.roles,name = "🎭Memes-dealer🧬")
            await member.remove_roles(role)

    def is_me(ctx):
        return ctx.author.id == 599076572745695233

    @commands.command()
    async def coinflip(self,ctx):
        num = random.randint(1,2)
        if(num==1):
            await ctx.send("Head")
        else:
            await ctx.send("Tail")


    @commands.command()
    async def rps(self,ctx,hand):
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

    @commands.command(aliases =["about"])
    async def help(self,ctx):
        myembed=discord.Embed(title="Commands", description = "All available commmands for Brian", color = discord.Color.dark_purple())
        myembed.set_thumbnail(url = "https://www.kindpng.com/picc/m/118-1189293_brian-griffin-brian-family-guy-hd-png-download.png")
        myembed.add_field(name = "`role",value = "Choose your Role by clicking on the Emojis",inline=False)
        myembed.add_field(name = "`coinflip",value = "Reply with Head or Tail",inline=False)
        myembed.add_field(name = "`rps",value = "Play a game of Rock Paper Scissor with Brian",inline=False)
        myembed.add_field(name = "`edit servername [Name]",value = "Rename the Server",inline=False)
        myembed.add_field(name = "`edit region [Region]",value = "Change the Region of the Server",inline=False)
        myembed.add_field(name = "`edit createtextchannel [Name]",value = "Create Text Channel with the given Name",inline=False)
        myembed.add_field(name = "`edit createvoicechannel [Name]",value = "Create Voice Channel with the given Name",inline=False)
        myembed.add_field(name = "`kick [Member]",value = "Kick a Member",inline=False)
        myembed.add_field(name = "`ban [Member]",value = "Ban a Member",inline=False)
        myembed.add_field(name = "`unban [Member]",value = "Unban a Member",inline=False)
        myembed.add_field(name = "`purge [Number]",value = "Delete [number] message(s)",inline=False)
        myembed.add_field(name = "`purge [Day] [Month]",value = "Delete all messages starting from that Date",inline=False)
        myembed.add_field(name = "`mute [Member]",value = "Mute a Member",inline=False)
        myembed.add_field(name = "`unmute [Member]",value = "Unmute a Member",inline=False)
        myembed.add_field(name = "`deafen [Member]",value = "Deafen a Member",inline=False)
        myembed.add_field(name = "`undeafen [Member]",value = "Undeafen a Member",inline=False)
        myembed.add_field(name = "`voicekick [Member]",value = "Kick a Member from a Voice Channel",inline=False)
        myembed.add_field(name = "`join",value = "Brian joins current Voice Channel",inline=False)
        myembed.add_field(name = "`leave",value = "Brian leaves current Voice Channel",inline=False)
        myembed.add_field(name = "`play [Music Name or Link]",value = "Play Music",inline=False)
        myembed.add_field(name = "`skip",value = "Skip current Music",inline=False)
        myembed.add_field(name = "`queue",value = "View Music Queue",inline=False)
        myembed.add_field(name = "`nowplaying",value = "View currently playing Music",inline=False)
        myembed.add_field(name = "`battleships [Member]",value = "Start a Battleships game with a Member",inline=False)
        myembed.add_field(name = "`place [position(s)]",value = "Place Ships on the board",inline=False)
        myembed.add_field(name = "`shoot [position]",value = "Shoot a Ship of the other Player",inline=False)
        myembed.add_field(name = "`poll [minute(s)] [Title]",value = "Create a Poll with two Options",inline=False)
        myembed.add_field(name = "`poll [minute(s)] [Title] [Options]",value = "Create a Poll with your Options",inline=False)

        await ctx.send(embed = myembed)

    @commands.group()
    async def edit(self,ctx):
        pass

    @edit.command()
    @commands.has_role("🥉Bro")
    async def servername(self,ctx,*,input):          # *,input get all after servername including space
        await ctx.guild.edit(name = input)

    @edit.command()
    async def region(self,ctx,*,input):          
        await ctx.guild.edit(region = input)

    @edit.command()
    async def createtextchannel(self,ctx,*,input):          
        await ctx.guild.create_text_channel(name = input)

    @edit.command()
    async def createvoicechannel(self,ctx,*,input):          
        await ctx.guild.create_voice_channel(name = input)

    @edit.command()
    async def createrole(self,ctx,*,input):          
        await ctx.guild.create_role(name = input)

    @commands.command()
    @commands.check(is_me)
    async def kick(self,ctx,mem : discord.Member,*,reason=None):
        await ctx.guild.kick(mem,reason=reason)

    @commands.command()
    @commands.check(is_me)
    async def ban(self,ctx,mem : discord.Member,*,reason=None):
        await ctx.guild.ban(mem,reason=reason)

    @commands.command()
    @commands.check(is_me)
    async def unban(self,ctx,*,input):
        name,discriminator = input.split("#")
        banned = await ctx.guild.bans()
        for bannedmem in banned:
            username = bannedmem.user.name
            disc = bannedmem.user.discriminator
            if name == username and discriminator == disc:
                await ctx.guild.unban(bannedmem.user)

    @commands.command()
    @commands.check(is_me)
    async def purge(self,ctx,amount,day : int=None,month : int=None,year : int=datetime.now().year):
        if amount == "/":
            if day==None or month==None:
                return
            else:
                await ctx.channel.purge(after = datetime(year,month,day))
        else:
            await ctx.channel.purge(limit = int(amount)+1)      # plus 1 to delete the `purge command


    @commands.command()
    @commands.has_role("🥉Bro")
    async def mute(self,ctx,mem : discord.Member):
        await mem.edit(mute=True)

    @commands.command()
    @commands.has_role("🥉Bro")
    async def unmute(self,ctx,mem : discord.Member):
        await mem.edit(mute=False)

    @commands.command()
    @commands.has_role("🥉Bro")
    async def deafen(self,ctx,mem : discord.Member):
        await mem.edit(deafen=True)

    @commands.command()
    @commands.has_role("🥉Bro")
    async def undeafen(self,ctx,mem : discord.Member):
        await mem.edit(deafen=False)

    @commands.command()
    @commands.has_role("🥉Bro")
    async def voicekick(self,ctx,mem : discord.Member):
        await mem.edit(voice_channel=None)


def setup(bot):
    bot.add_cog(ServerManagementCog(bot))