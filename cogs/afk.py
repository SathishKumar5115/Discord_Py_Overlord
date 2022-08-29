import discord
from discord import client
from discord.ext import commands
import random
import json
import time

def get_prefix(client, message):

  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)

  return prefixes[str(message.guild.id)]

intents = discord.Intents.default() 
intents.members = True
client = commands.Bot(command_prefix = get_prefix, case_insensitive = True, intents=intents)

class AFK(commands.Cog):
    '''
    Class containing AFK commands/system.
    '''
    def __init__(self, client, *args, **kwargs):
        self.client = client
    #*
    async def update_data(self, afk, user):
        if not f'{user.id}' in afk:
            afk[f'{user.id}'] = {}
            afk[f'{user.id}']['AFK'] = 'False'
            afk[f'{user.id}']['reason'] = 'None'
    
    async def time_formatter(self, seconds: float):
        '''
        Convert UNIX time to human readable time.
        '''
        minutes, seconds = divmod(int(seconds), 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        tmp = ((str(days) + "d, ") if days else "") + \
            ((str(hours) + "h, ") if hours else "") + \
            ((str(minutes) + "m, ") if minutes else "") + \
            ((str(seconds) + "s, ") if seconds else "")
        return tmp[:-2]
    
    @commands.Cog.listener()
    async def on_message(self, message):
        with open('afk.json', 'r') as f:
            afk = json.load(f)
        
        for user_mention in message.mentions:

            if not f'{user_mention.id}' in afk:
               return

            if afk[f'{user_mention.id}']['AFK'] == 'True':
                if message.author.bot: 
                    return
                
                reason = afk[f'{user_mention.id}']['reason']
                meth = int(time.time()) - int(afk[f'{user_mention.id}']['time'])
                been_afk_for = await self.time_formatter(meth)
                embed = discord.Embed(title = '💤 User Afk', description=f'{user_mention.name} Is currently AFK!')
                embed.add_field(name='Reason :', value=f'{reason}', inline=False)
                embed.set_thumbnail(url= user_mention.avatar.url)

                await message.channel.send(content=message.author.mention, embed=embed)
                
                meeeth = int(afk[f'{user_mention.id}']['mentions']) + 1
                afk[f'{user_mention.id}']['mentions'] = meeeth
                with open('afk.json', 'w') as f:
                    json.dump(afk, f)
        
        if not message.author.bot:
            await self.update_data(afk, message.author)

            if afk[f'{message.author.id}']['AFK'] == 'True':
                
                meth = int(time.time()) - int(afk[f'{message.author.id}']['time'])
                been_afk_for = await self.time_formatter(meth)
                mentionz = afk[f'{message.author.id}']['mentions']

                embed = discord.Embed(title = f'👋 Welcome Back {message.author.name}!', color=message.author.color)
                embed.add_field(name="You've been AFK for :", value=been_afk_for, inline=False)
                
                embed.set_thumbnail(url= message.author.avatar.url)
                
                await message.channel.send(content=message.author.mention, embed=embed)
                embed2=discord.Embed(title='Mentions while AFK :', description=mentionz)
                await message.author.send(embed=embed2)

                
                afk[f'{message.author.id}']['AFK'] = 'False'
                afk[f'{message.author.id}']['reason'] = 'None'
                afk[f'{message.author.id}']['time'] = '0'
                afk[f'{message.author.id}']['mentions'] = 0
                
                with open('afk.json', 'w') as f:
                    json.dump(afk, f)
                
                try:
                    await message.author.edit(nick=f'{message.author.display_name[5:]}')
                except:
                    pass
        
        with open('afk.json', 'w') as f:
            json.dump(afk, f)

    @client.hybrid_command(name = "afk",with_app_command = True)     
    async def afk(self, ctx, *, reason=None):
        with open('afk.json', 'r') as f:
            afk = json.load(f)
        if afk[f'{ctx.author.id}']['AFK'] == 'True':        
             return
        if not reason:
            reason = 'None'
             
        await self.update_data(afk, ctx.message.author)
        afk[f'{ctx.author.id}']['AFK'] = 'True'
        afk[f'{ctx.author.id}']['reason'] = f'{reason}'
        afk[f'{ctx.author.id}']['time'] = int(time.time())
        afk[f'{ctx.author.id}']['mentions'] = 0

        embed = discord.Embed(title = '💤 User AFK',description=f"I've set your AFK {ctx.message.author.name}!", color=ctx.author.color)
        embed.add_field(name='Reason :', value=f'{reason}', inline=False)
        embed.set_thumbnail(url= ctx.author.avatar.url)
        await ctx.send(content=ctx.message.author.mention, embed=embed)

        with open('afk.json', 'w') as f:
            json.dump(afk, f)
        try:
            await ctx.author.edit(nick=f'[AFK]{ctx.author.display_name}')
        except:
            pass
        

async def setup(client):
    await client.add_cog(AFK(client))