# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
from discord.ext import commands
import secrets

TOKEN = secrets.token
BOT_PREFIX = ("!")

client = commands.Bot(command_prefix=BOT_PREFIX)

@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
