import disnake
from disnake.ext import commands


class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.slash_command()
    async def help(self, inter):
        embed = disnake.Embed(title='Help', description=f'Help info for {self.client.user.name}')
        for command in self.client.slash_commands:
            description = command.description
            if not description or description == None or description == '-':
                description = 'No description'
            embed.add_field(name=command.name, value=description)
        await inter.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
