from discord.ext import commands
import discord
class ServerManagementCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("BOT IS ONLINE")

    @commands.Cog.listener()
    async def on_message(self,msg):
        username = msg.author.display_name
        if msg.author == self.bot.user:
            return
        else:
            if msg.content == "`role":
                new_msg = await msg.channel.send("Lord - 🍇\nBro - 🍓\nDJ - 🍈\nChecker - 🍆\nMemes-dealer - 🥥")
                await new_msg.add_reaction("🍇")
                await new_msg.add_reaction("🍓")
                await new_msg.add_reaction("🍈")
                await new_msg.add_reaction("🍆")
                await new_msg.add_reaction("🥥")
            if msg.content == "hello":
                await msg.channel.send("Hello " + username)

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


def setup(bot):
    bot.add_cog(ServerManagementCog(bot))