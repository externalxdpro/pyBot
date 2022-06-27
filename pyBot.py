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


# Print a message on startup
@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')

# Load commands
extensions = []

for file in os.listdir('./commands'):
    if file.endswith('.py'):
        extensions.append('commands.' + file[:-3])

if __name__ == '__main__':
    for extension in extensions:
        client.load_extension(extension)

# Log the bot in
client.run(token)
