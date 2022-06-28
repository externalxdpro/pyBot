import disnake
from disnake.ext import commands


class Kick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.slash_command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, inter, user: disnake.User, reason: str = None):
        """
        Kick a user from the server

        Parameters
        ----------
        user: The user to kick
        reason: The reason for the kick
        """
        if reason == None:
            reason = 'No reason specified'
        await inter.guild.kick(user=user, reason=reason)
        await inter.response.send_message(f'User {user.mention} has been kicked for {reason}')


def setup(bot):
    bot.add_cog(Kick(bot))
