import disnake
from disnake.ext import commands


class Ban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.slash_command()
    @commands.has_permissions(kick_members=True)
    async def ban(self, inter, user: disnake.User, reason: str = None):
        """
        Ban a user from the server

        Parameters
        ----------
        user: The user to ban
        reason: The reason for the ban
        """
        if reason == None:
            reason = 'No reason specified'
        await inter.guild.ban(user=user, reason=reason)
        await inter.response.send_message(f'User {user.mention} has been banned for {reason}')
        try:
            await user.dm_channel.send(f'You have been banned from {inter.guild.name} for {reason}')
        except AttributeError:
            await user.create_dm()
            await user.dm_channel.send(f'You have been banned from {inter.guild.name} for {reason}')


def setup(bot):
    bot.add_cog(Ban(bot))
