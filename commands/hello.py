import disnake
from disnake.ext import commands


class Hello(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.slash_command()
    async def hello(self, inter):
        """Says hello."""
        await inter.response.send_message('ello mate')


def setup(bot):
    bot.add_cog(Hello(bot))
