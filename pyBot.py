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


@client.slash_command(name='8ball')
async def eight_ball(inter, question: str):
    """
    Give a random response to a question.

    Parameters
    ----------
    question: The question you want the wise 8-ball to answer
    """
    import random

    answers = [
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]

    title = '8-Ball'
    desc = f'Question: {question}\nAnswer: {random.choice(answers)}'
    embed = disnake.Embed(title=title, description=desc)
    await inter.response.send_message(embed=embed)


@client.slash_command()
async def hello(inter):
    """Says hello."""
    await inter.response.send_message('ello mate')


@client.slash_command()
async def ping(inter):
    """Output the bot's ping."""
    await inter.response.send_message('Ping!\nPing: {0}'.format(round(client.latency, 2)))


@client.slash_command()
async def whois(inter, user: disnake.User = None):
    """
    Output user info of a user.

    Parameters
    ----------
    user: The user to get info about
    """
    if user == None:
        user = inter.user

    title = 'Whois'
    desc = f'User info for {user}'
    colour = user.colour
    serverName = str(inter.guild.name)
    avatar = user.display_avatar.url
    createdAt = user.created_at

    embed = disnake.Embed(title=title, description=desc)
    embed.set_default_colour(colour)
    embed.set_footer(text=serverName)
    embed.set_thumbnail(url=avatar)
    embed.add_field(name='Full Username:', value=user)
    embed.add_field(name='ID:', value=user.id)
    embed.add_field(name='Account Creation Date:', value=createdAt, inline=False)
    embed.add_field(name='Bot:', value=user.bot)
    embed.set_author(name=inter.user)
    await inter.response.send_message(embed=embed)

client.run(token)
