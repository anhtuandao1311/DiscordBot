import discord
from discord.ext import commands
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "`",help_command=None,intents = intents)

@bot.command
async def reload(ctx):
    bot.reload_extension("ServerManagementCog")
    bot.reload_extension("MusicCog")
    bot.reload_extension("PollCog")
    bot.reload_extension("BattleshipsCog")

bot.load_extension("ServerManagementCog")
bot.load_extension("MusicCog")
bot.load_extension("BattleshipsCog")
bot.load_extension("PollCog")


bot.run("Your Token")