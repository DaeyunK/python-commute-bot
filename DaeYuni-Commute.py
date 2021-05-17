#pip install discord
#pip install datetime
#pip install commands
import discord
import datetime
from discord.ext import commands

app = commands.Bot(command_prefix='-', case_insensitive=True, help_command=None)

@app.event
async def on_ready():
    game = discord.Game('서술')
    await app.change_presence(status=discord.Status.online, activity=game)

@app.command()
async def 출근(ctx):
        embed = discord.Embed(title=f"{ctx.author} 님 출/퇴근 관리", description="출근이 정상적으로 처리 되었습니다.", timestamp=datetime.datetime.utcnow(), colour=discord.Colour.green())
        await ctx.reply(embed=embed, mention_author=True)

@app.command()
async def 퇴근(ctx):
        embed = discord.Embed(title=f"{ctx.author} 님 출/퇴근 관리", description="퇴근이 정상적으로 처리 되었습니다.", timestamp=datetime.datetime.utcnow(), colour=discord.Colour.red())
        await ctx.reply(embed=embed, mention_author=True)


app.run("TOKEN")
