#!/usr/bin/env python3

import os
import logging
import disnake
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")

logger = logging.getLogger('disnake')
handler = logging.FileHandler(filename='pyBot.log', encoding='utf-8', mode='w')
logger.addHandler(handler)
logger.setLevel(logging.INFO)

intents = disnake.Intents.all()
client = disnake.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(f'Message from {message.author}: {message.content}')

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(token)
