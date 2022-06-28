import disnake
from disnake.ext import commands


class EightBall(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.slash_command(name='8ball')
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


def setup(client):
    client.add_cog(EightBall(client))
