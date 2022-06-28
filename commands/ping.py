import disnake
from disnake.ext import commands


class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.slash_command()
    async def ping(self, inter):
        """Output the bot's ping."""
        # await inter.response.send_message('Ping!\nPing: {0}'.format(round(commands.Bot.latency, 2)))
        await inter.response.send_message(f'Ping!\nPing: {commands.Bot.latency}')


def setup(bot):
    bot.add_cog(Ping(bot))
