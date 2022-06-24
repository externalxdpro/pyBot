#!/usr/bin/env python3

import os
import logging
import disnake
from disnake.ext import commands
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")
guildId = os.getenv("GUILDID")

logger = logging.getLogger('disnake')
handler = logging.FileHandler(filename='pyBot.log', encoding='utf-8', mode='w')
logger.addHandler(handler)
logger.setLevel(logging.INFO)

intents = disnake.Intents.all()
client = commands.InteractionBot(test_guilds=[int(guildId)], intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')

@client.slash_command()
async def hello(inter):
    await inter.response.send_message('Hello!')

client.run(token)
