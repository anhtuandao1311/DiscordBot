import discord
from discord.ext import commands,tasks
class PollCog(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        self.numbers=["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]

    @commands.command()
    async def poll(self,ctx,minutes:int,title,*options):
        if len(options)==0:
            pollembed = discord.Embed(title = title,description = f"You have ** {minutes} ** minutes remaining!")
            msg = await ctx.send(embed = pollembed)
            await msg.add_reaction("👍")
            await msg.add_reaction("👎")
        else:
            pollembed = discord.Embed(title = title,description = f"You have ** {minutes} ** minutes remaining!")
            for number,option in enumerate(options):
                pollembed.add_field(name = f"{self.numbers[number]}",value = f"**{option}**",inline = False)
            msg = await ctx.send(embed = pollembed)
            for x in range(len(pollembed.fields)):
                await msg.add_reaction(f"{self.numbers[x]}")
        self.poll_loop.start(ctx,minutes,title,options,msg)
        
    @tasks.loop(minutes = 1)
    async def poll_loop(self,ctx,minutes,title,options,msg):
        count = self.poll_loop.current_loop
        remain = minutes - count
        newembed = discord.Embed(title = title,description = f"You have ** {remain} ** minutes remaining!")
        for number,option in enumerate(options):
            newembed.add_field(name = f"{self.numbers[number]}",value = f"**{option}**",inline = False)
            await msg.edit(embed = newembed)
        if remain == 0:
            counts = []
            msg = discord.utils.get(self.bot.cached_messages,id = msg.id)
            reactions = msg.reactions
            for reaction in reactions:
                counts.append(reaction.count)
            maxval = max(counts)
            i=0
            for count in counts:
                if count == maxval:
                    i=i+1
            if i>1:
                await ctx.send("It's a draw!")
            else:
                maxid = counts.index(maxval)
                if len(options)==0:
                    winner = reactions[maxid]
                    if winner.emoji == "👍":
                        await ctx.send("Factos👍")
                    if winner.emoji == "👎":
                        await ctx.send("Not Factos👎")
                else:
                    winner = options[maxid]
                    emoji = reactions[maxid]
                    await ctx.send("Time's up!")
                    await ctx.send(f"{emoji} **{winner}** has won the poll!")
            self.poll_loop.stop()
                    


def setup(bot):          
    bot.add_cog(PollCog(bot))