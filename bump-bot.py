import asyncio, discord
from discord.ext import commands
import time

client = commands.Bot(command_prefix='-')
channel = client.get_channel(id=857905253348409355)
status = False

@client.event
async def bump():
    global channel
    while status == True:
        await channel.send("!d bump")
        await asyncio.sleep(5)

@client.event
async def on_ready():
    print('bot online')
    await bump()

@client.event
async def on_guild_join(guild):
    await helpsheet('idk')

@client.command()
async def bumpbot(ctx):
    global channel
    global status
    channel = client.get_channel(id=857905253348409355)
    on_off = True if str(ctx.message.content.split(' ')[1]) == 'on' else False
    msg_color = discord.Color.green() if on_off == True else discord.Color.red()
    status = on_off # change bot on/off status

    embed = discord.Embed(title=("BumpBot is now "+str(status)), color = msg_color)
    await channel.send(embed=embed) # send embedded msg to
    await bump()

@client.command()
async def helpsheet(ctx):
    global channel
    embed = discord.Embed(title="__BumpBot Help Sheet__", description="Please refer to this sheet when using the BumpBot :)", color=discord.Color.purple()) #,color=Hex code
    embed.add_field(name="`-helpsheet`", value="Brings up this sheet!")
    embed.add_field(name="`-bumpbot [on/off]`", value="Turn the bot on or off.")
    await client.get_channel(id=857905253348409355).send(embed=embed)

client.run('insert token')
