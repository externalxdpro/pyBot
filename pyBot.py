#!/usr/bin/env python3

# Imports
import os
import logging
import disnake
from disnake.ext import commands
from dotenv import load_dotenv

# Get environment variables from .env
load_dotenv()
token = os.getenv("TOKEN")
guildId = os.getenv("GUILDID")

# Set up logger
logger = logging.getLogger('disnake')
handler = logging.FileHandler(filename='pyBot.log', encoding='utf-8', mode='w')
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Set up intents and client
intents = disnake.Intents.all()
client = commands.InteractionBot(test_guilds=[int(guildId)], intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')


@client.slash_command()
async def hello(inter):
    """Says hello."""
    await inter.response.send_message('ello mate')


@client.slash_command()
async def ping(inter):
    """Output the bot's ping."""
    await inter.response.send_message('Ping!\nPing: {0}'.format(round(client.latency, 2)))

client.run(token)
