import discord
from discord.ext import commands
import json

intents = discord.Intents.default()
intents.message_content = True

def get_prefix(client, message):

  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)

  return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix, case_insensitive = True, intents=intents,allowed_mentions = discord.AllowedMentions(everyone = bool))

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_guild_join(guild):

  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)
  
  prefixes[str(guild.id)] = "?"

  with open("prefixes.json", "w") as f:
    json.dump(prefixes,f)

@client.event
async def on_message(msg):

    if client.user.id in msg.raw_mentions:

        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)
        try:
            pre = prefixes[str(msg.guild.id)]
        except:
            prefixes[str(msg.guild.id)] = "?"

            with open("prefixes.json", "w") as f:
                json.dump(prefixes,f)
            with open("prefixes.json", "r") as f:
                prefixes = json.load(f)
            
            pre = prefixes[str(msg.guild.id)]

            await msg.channel.send(f"My prefix for this server is **`{pre}`**. Use **`{pre}help`** for more info.")
        
@client.command()
@commands.cooldown(1,5,commands.BucketType.user)
@commands.has_permissions(administrator = True)
async def setprefix(ctx, prefix):

  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)
  
  prefixes[str(ctx.guild.id)] = prefix

  with open("prefixes.json", "w") as f:
    json.dump(prefixes,f)
  embed = discord.Embed(title = " Prefix Changed ", description = f"**The prefix for this server was changed to {prefix}**",color = ctx.author.color)
  await ctx.reply(embed=embed)

client.run('MTAxMjkwMzg4NTU1NzQ4NTYxOQ.Gbqa3z.soBOVvNdhfEcO7IME0BRVfoA1y_1cBZ6_hMkjs')