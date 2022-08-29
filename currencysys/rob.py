import discord
from discord.ext import commands
import json
import random
from currencysys import money

def get_prefix(client, message):

  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)

  return prefixes[str(message.guild.id)]

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = get_prefix, case_insensitive = True, intents=intents,allowed_mentions = discord.AllowedMentions(everyone = bool))

@client.hybrid_command(name = "rob", description="😈 Rob a user 😈",with_app_command = True)
@commands.cooldown(1,120,commands.BucketType.user)
async def rob(ctx,member:discord.Member):
    await money.open_account(ctx.author)
    await money.open_account(member)
   
    bal = await money.update_bank(member)
    if bal[0]<100:
        await ctx.send("They are too poor to rob")
        return
    
    earnings = random.randrange(0, bal[0])
    
    await money.update_bank(ctx.author,earnings)
    await money.update_bank(member,-1*earnings)
    
    await ctx.send(f"You robbed {member} and got **Ⓥ** {earnings} coins!")

async def setup(client):
     client.add_command(rob)