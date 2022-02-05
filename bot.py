import os
import discord

from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

client = commands.Bot()
slash = SlashCommand(client, sync_commands=True)

BOT_TOKEN = os.getenv('RES_BOT_TOKEN')

@client.event
async def on_ready():
    print(f'{client.user} is now connected to Discord!')

client.run(BOT_TOKEN)