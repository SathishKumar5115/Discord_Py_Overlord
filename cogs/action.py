import discord
import random
from discord.ext import commands
import json
import aiohttp
from discord.ext.commands import cooldown, BucketType
import asyncio
from discord import Embed

def get_prefix(client, message):

  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)

  return prefixes[str(message.guild.id)]

intents = discord.Intents.default() 
intents.members = True
client = commands.Bot(command_prefix = get_prefix, case_insensitive = True, intents=intents)

class actions(commands.Cog):

    def __init__(self, client):
        self.client = client

    @client.hybrid_command(name = "highfive",description="🙌 HighFive 🙌",with_app_command = True)
    @commands.cooldown(1,5,commands.BucketType.user)
    async def highfive(self, ctx, *,  member : discord.Member=None):
          if member == None:
            msg = 'You need to mention a user.'
            await ctx.channel.send(msg)
            return

          responses = [    "https://cdn.weeb.sh/images/B1-7KkQsZ.gif",
                  "https://cdn.weeb.sh/images/r1MMK1msb.gif",
                  "https://cdn.weeb.sh/images/rJYQt1mjZ.gif" ]
          randnum = random.randint(0, len(responses)-1)
          msg = '{}'.format(responses[randnum])
          embed = discord.Embed(title = f" {ctx.author.name} gives {member.name} a highfive! ",color = ctx.author.color)
          embed.set_image(url = msg)
          await ctx.send(embed=embed)  


    @client.hybrid_command(name = "slap",description="🎯 Slap 🎯",with_app_command = True)
    @commands.cooldown(1,5,commands.BucketType.user)
    async def slap(self, ctx, *,  member : discord.Member):
          if member == None:
            msg = 'You need to mention a user.'
            await ctx.channel.send(msg)
            return

          responses = [    "https://cdn.weeb.sh/images/HJKiX1tPW.gif",
                  "https://cdn.weeb.sh/images/rJ4141YDZ.gif",
                  "https://cdn.weeb.sh/images/ByTR7kFwW.gif",
                  "https://cdn.weeb.sh/images/BJgsX1Kv-.gif"]
          randnum = random.randint(0, len(responses)-1)
          msg = '{}'.format(responses[randnum])
          embed = discord.Embed(title = f" {ctx.author.name} slaps {member.name}",color = ctx.author.color)
          embed.set_image(url = msg)
          await ctx.send(embed=embed)  
          

    @client.hybrid_command(name = "greet",description="👋 Greet 👋",with_app_command = True)
    @commands.cooldown(1,5,commands.BucketType.user)
    async def greet(self, ctx, *,  member : discord.Member):
          if member == None:
            msg = 'You need to mention a user.'
            await ctx.channel.send(msg)
            return

          responses = [    "https://cdn.weeb.sh/images/Skc7rj3AZ.gif",
                  "https://cdn.weeb.sh/images/SkK5Is2Rb.gif",
                  "https://cdn.weeb.sh/images/HJrmronAZ.gif",
                  "https://cdn.weeb.sh/images/HJ794ohR-.gif" ]
          randnum = random.randint(0, len(responses)-1)
          msg = '{}'.format(responses[randnum])
          embed = discord.Embed(title = f" {ctx.author.name} waves at {member.name}",color = ctx.author.color)
          embed.set_image(url = msg)
          await ctx.send(embed=embed)  

    @client.hybrid_command(name = "kill",description="🔪 Kill 🔪",with_app_command = True)
    @commands.cooldown(1,5,commands.BucketType.user)
    async def kill(self, ctx, *,  member : discord.Member):
          if member == None:
            msg = 'You need to mention a user.'
            await ctx.channel.send(msg)
            return

          responses = [    "https://cdn.weeb.sh/images/HyXTiyKw-.gif",
                  "https://cdn.weeb.sh/images/B1VnoJFDZ.gif",
                  "https://cdn.weeb.sh/images/BJO2j1Fv-.gif",
                  "https://cdn.weeb.sh/images/r11as1tvZ.gif" ]
          randnum = random.randint(0, len(responses)-1)
          msg = '{}'.format(responses[randnum])
          embed = discord.Embed(title = f" {ctx.author.name} killed {member.name}! Oof",color = ctx.author.color)
          embed.set_image(url = msg)      
          await ctx.send(embed=embed)  

    @client.hybrid_command(name = "hug",description="🫂 Hug 🫂",with_app_command = True)
    @commands.cooldown(1,5,commands.BucketType.user)
    async def hug(self, ctx, *,  member : discord.Member):
          if member == None:
            msg = 'You need to mention a user.'
            await ctx.channel.send(msg)
            return

          responses = [    "https://cdn.weeb.sh/images/BkZCSI7Pb.gif",
                  "https://cdn.nekos.life/hug/hug_079.gif",
                  "https://cdn.nekos.life/hug/hug_012.gif"]
          randnum = random.randint(0, len(responses)-1)
          msg = '{}'.format(responses[randnum])
          embed = discord.Embed(title = f" {ctx.author.name} gives {member.name} a big hug!",color = ctx.author.color)
          embed.set_image(url = msg)       
          await ctx.send(embed=embed)  

async def setup(client):
  await client.add_cog(actions(client))