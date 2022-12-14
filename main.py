import discord
from discord.ext import commands
import json
import os
import asyncio
import logging
from dotenv import load_dotenv
import os

def get_prefix(client, message):

  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)
  return prefixes[str(message.guild.id)]

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = get_prefix, case_insensitive = True, intents=intents,allowed_mentions = discord.AllowedMentions(everyone = bool))

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await client.load_extension(f"cogs.{filename[:-3]}")
    for filename in os.listdir("./currencysys"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await client.load_extension(f"currencysys.{filename[:-3]}")

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
        await msg.channel.send(f"My prefix for this server is **`{pre}`**. Use **`{pre}help`** or **`/helpmenu`** for more info.")
        
    await client.process_commands(msg)

@client.event
async def setup_hook():
    await client.tree.sync()
    print(f"Synced slash commands for {client.user}")

@client.hybrid_command(name = "setprefix",description="Change bot prefix for this server",with_app_command = True)
@commands.cooldown(1,5,commands.BucketType.user)
@commands.has_permissions(administrator = True)
async def setprefix(ctx : commands.Context, prefix):
 
  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)
  
  prefixes[str(ctx.guild.id)] = prefix

  with open("prefixes.json", "w") as f:
    json.dump(prefixes,f)
  embed = discord.Embed(title = " Prefix Changed ", description = f"**The prefix for this server was changed to {prefix}**",color = ctx.author.color)
  await ctx.reply(embed=embed)

@client.hybrid_command(name = "allcommands",description="Check all commands",with_app_command = True)
async def allcommands(ctx):
    helptext = "```"
    for command in client.commands:
        helptext+=f"{command}\n"
    helptext+="```"
    await ctx.send(helptext)

client.remove_command("help")

load_dotenv('.env')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

async def main():
        await load_extensions()

asyncio.run(main())
client.run(os.getenv('BOT_TOKEN'),log_handler=handler)
