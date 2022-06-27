from disnake.ext import commands


class Whois(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.slash_command()
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
        joinedAt = user.joined_at

        embed = disnake.Embed(title=title, description=desc)
        embed.set_default_colour(colour)
        embed.set_footer(text=serverName)
        embed.set_thumbnail(url=avatar)
        embed.add_field(name='Full Username:', value=user)
        embed.add_field(name='ID:', value=user.id)
        embed.add_field(name='Account Creation Date:', value=createdAt, inline=False)
        embed.add_field(name='Joined Server Date:', value=joinedAt)
        embed.add_field(name='Bot:', value=user.bot)
        embed.set_author(name=inter.user)
        await inter.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(Whois(bot))
