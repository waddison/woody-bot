# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
from discord.ext import commands
import secrets
import riotservice

TOKEN = secrets.token
BOT_PREFIX = ("!")

client = commands.Bot(command_prefix=BOT_PREFIX)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.command()
async def info():
    embed = discord.Embed(title="Woody's bot", description="Doing a little bit of practice here")

    embed.add_field(name="Author", value="Woody!")
    embed.add_field(name="2nd column", value="2nd description")

    await client.say(embed=embed)


@client.command()
async def source_code():
    await client.say(secrets.github)

@client.command()
async def greet(user: discord.User=None):
    if not user:
        await client.say("Hello everybody!")
    else:
        await client.say(f"Hello {user.display_name}!")

@client.command()
async def lol_summoner(summonerName: str=None):
    summoner = riotservice.get_summoner(summonerName)

    await client.say(f"League of Legends summoner {summoner['name']} is level {summoner['summonerLevel']}")


client.run(TOKEN)
