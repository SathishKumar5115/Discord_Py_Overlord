from discord.ext import commands
from discord import Embed
import discord
import json

def to_emoji(c):
    base = 0x1f1e6
    return chr(base + c)

def get_prefix(client, message):

  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)

  return prefixes[str(message.guild.id)]

intents = discord.Intents.default() 
intents.members = True
client = commands.Bot(command_prefix = get_prefix, case_insensitive = True, intents=intents)

class Polls(commands.Cog):


    def __init__(self, client):
        self.client = client

    @client.hybrid_command(name = "poll",description="Create a poll.First question and followed by options each seperated by a comma( , )",with_app_command = True)  
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def poll(self, ctx, string: str):
        
        questions_and_choices = string.split(",")
        if len(questions_and_choices) < 2:
            return await ctx.send('Need at least 1 question with 2 choices.')
        elif len(questions_and_choices) > 21:
            return await ctx.send('You can only have up to 20 choices.')

        perms = ctx.channel.permissions_for(ctx.me)
        if not (perms.read_message_history or perms.add_reactions):
            return await ctx.send('Need Read Message History and Add Reactions permissions.')

        question = questions_and_choices[0]
        choices = [(to_emoji(e), v) for e, v in enumerate(questions_and_choices[1:])]

        try:
            await ctx.message.delete()
        except:
            pass


        body = "\n".join(f"{key}: {c}" for key, c in choices)
        embed = discord.Embed(title = f"{question}",description = f"{body}",color = ctx.author.color)
        embed.set_footer(text = f'Poll by {ctx.author}', icon_url = f'{ctx.author.avatar.url}')     
        poll = await ctx.send(embed=embed)
        for emoji, _ in choices:
            await poll.add_reaction(emoji)

async def setup(bot):
   await bot.add_cog(Polls(bot))