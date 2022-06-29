import discord
from discord.ext import commands
from discord.ext.commands.core import Command
from discord.ext.commands.errors import CommandInvokeError
class BattleshipsCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.playing = False
        self.board1=""
        self.board2=""
        self.boardtoshow1=""
        self.boardtoshow2=""
        self.turn=""


    async def render(self,ctx,board):
        numbers = [":one:",":two:",":three:",":four:",":five:",":six:",":seven:",":eight:",":nine:",":ten:"]

        alphabets = [":regional_indicator_a:",":regional_indicator_b:",":regional_indicator_c:",":regional_indicator_d:",":regional_indicator_e:",":regional_indicator_f:",":regional_indicator_g:",
        ":regional_indicator_h:",":regional_indicator_i:",":regional_indicator_j:"]

        stringboard = ""
        stringboard = stringboard + ":black_medium_small_square:"
        for x in range(len(board[0])):
            stringboard = stringboard + alphabets[x]
        stringboard = stringboard + "\n"
        i = 0
        for row in board:
            stringboard = stringboard + numbers[i]
            i = i+1
            for square in row:
                stringboard = stringboard + square
            stringboard = stringboard + "\n"
        await ctx.send(stringboard)

    

    @commands.command()
    async def battleships(self,ctx,player2 : discord.Member, ver : int = 5,hor : int = 5):
        if self.playing == False:
            self.playing=True
            self.player1 = ctx.author
            self.player2 = player2
            self.turn = self.player1
            self.board1 = [[":blue_square:"]*hor for x in range(ver)]
            self.board2 = [[":blue_square:"]*hor for x in range(ver)]
            self.boardtoshow1 = [[":blue_square:"]*hor for x in range(ver)]
            self.boardtoshow2 = [[":blue_square:"]*hor for x in range(ver)]
            await self.render(self.player1,self.board1)
            await self.render(self.player2,self.board2)
            await self.player1.send("Welcome to Battleships! Type ** `place ** to place your ships, letters go first then numbers (Ex: A1)")
            await self.player2.send("Welcome to Battleships! Type ** `place ** to place your ships, letters go first then numbers (Ex: A1)")
        else:
            await ctx.send("A game is already in progress!")

    def shipcount(self,board):
        count = 0
        for row in board:
            for square in row:
                if square == ":ship:":
                    count = count + 1
        return count

    @commands.command()
    async def place(self,ctx,*coordinate):     # *coordinate take all after command, separate by space and put them into a tuple
        if self.playing==True:
            if ctx.author == self.player1:
                board = self.board1
            if ctx.author == self.player2:
                board = self.board2
            if len(coordinate) == 0:
                await ctx.send("please type in the coordinates")
            else:
                if self.shipcount(board)==6:
                        await ctx.send("You can only place 6 ships")
                else:
                    for coor in coordinate:
                        alphabet = coor[0].lower()
                        number = coor[1]
                        x = ord(alphabet) - 97
                        y = int(number) - 1
                        board[y][x] = ":ship:"
                await self.render(ctx.author,board)
        else:
            await ctx.send("Please start a game by typing ** `battleships **")
    @commands.command()
    async def shoot(self,ctx,coor):
        if self.turn == ctx.author:
            if self.playing==True:
                if ctx.author == self.player1:
                    boardtoshoot = self.board2
                    boardtoshow = self.boardtoshow2
                    next = self.player2
                if ctx.author == self.player2:
                    boardtoshoot = self.board1
                    boardtoshow = self.boardtoshow1
                    next = self.player1

                alphabet = coor[0].lower()
                number = coor[1]
                x = ord(alphabet) - 97
                y = int(number) - 1
                if boardtoshoot[y][x] == ":ship:":
                    await ctx.send("Hit!")
                    boardtoshoot[y][x] = ":boom:"
                    boardtoshow[y][x] = ":boom:"
                if boardtoshoot[y][x] == ":blue_square:":
                    await ctx.send("Miss!")
                    boardtoshoot[y][x] = ":white_medium_square:"
                    boardtoshow[y][x] = ":white_medium_square:"
                    self.turn = next
                    if ctx.author == self.player1:
                        await self.player2.send("Player 1 missed! Your turn")
                    if ctx.author == self.player2:
                        await self.player1.send("Player 2 missed! Your turn")
                if boardtoshoot[y][x] == ":boom:" or boardtoshoot[y][x] == ":white_medium_square:":
                    await ctx.send("You shot this square before")
                await self.render(ctx.author,boardtoshow)
                if self.shipcount(boardtoshoot)==0:
                    self.playing=False
                    if ctx.author == self.player1:
                        await self.player1.send("You have won the game!")
                        await self.player2.send("You have lost the game!")
                        await self.render(self.player2,self.board1)
                    if ctx.author == self.player2:
                        await self.player2.send("You have won the game!")
                        await self.player1.send("You have lost the game!")
                        await self.render(self.player1,self.board2)
            else:
                await ctx.send("Please start a game by typing ** `battleships **")
        else:
            await ctx.send("It's not your turn!")     


    # Error
    @battleships.error
    async def errorhandler(self,ctx,error):
        if isinstance(error,commands.errors.MissingRequiredArgument):
            await ctx.send("Please mention the second player.")
    
    @shoot.error
    async def errorhandler(self,ctx,error):
        if isinstance(error,commands.errors.MissingRequiredArgument):
            await ctx.send("Please define the coordinate")
 
    @place.error
    async def errorhandler(self,ctx,error):
        if isinstance(error,commands.errors.CommandInvokeError):
            await ctx.send("Please type in a proper coordinate")

def setup(bot):
    bot.add_cog(BattleshipsCog(bot))