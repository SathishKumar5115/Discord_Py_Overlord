import discord
from discord.ext import commands
import json
import time

def get_prefix(client, message):

  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)

  return prefixes[str(message.guild.id)]

intents = discord.Intents.default() 
intents.members = True
client = commands.Bot(command_prefix = get_prefix, case_insensitive = True, intents=intents)

def revert(time):
    if time <= 86400 and time >3600:
        hrs = time//3600
        mins = (time%3600)/60
        return f"**{int(hrs)} hour(s) {int(mins)} minute(s)**"
    elif time <= 3600 and time >60:
        times = time//60
        secs = (time%60)
        secs = str(secs)[:2]
        times = f"**{int(times)} minute(s) {secs} second(s)**"
        return times
    elif time<=60:
        return f"**{int(time)} second(s) Left !**"

class misc(commands.Cog):
    '''
    Class containing AFK commands/system.
    '''
    def __init__(self, client, *args, **kwargs):
        self.client = client


    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        with open("prefixes.json", "r") as f:
          prefixes = json.load(f)
        
        prefix = prefixes[str(ctx.guild.id)]
        if str(ctx.guild.id) in prefix:
            prefix = prefix[str(ctx.guild.id)]
        else:
            prefix = "?"
        if not isinstance(error, commands.CommandOnCooldown):
            try:
                ctx.command.reset_cooldown(ctx)
            except:
                pass
        if isinstance(error ,commands.MissingPermissions):
            await ctx.send(embed = discord.Embed(description = "You do not have the required Permissions to Use this command.",color=ctx.author.colour),delete_after = 10,ephemeral=True)
            await ctx.message.delete() 
        elif isinstance(error,commands.errors.ChannelNotFound):
            await ctx.send(embed = discord.Embed(title = "Channe not found!",description = "No such Text Channel exists\nPlease Type #channel_name to Mention a Channel",color = ctx.author.colour),ephemeral=True)
        elif isinstance(error , commands.errors.MemberNotFound):
            await ctx.send(embed = discord.Embed(description="Member not found!!",color=ctx.author.colour,delete_after = 10),ephemeral=True)
            await ctx.message.delete()
        elif isinstance(error , commands.errors.CommandNotFound):
            pass
        elif isinstance(error, commands.CommandOnCooldown):
            msg = revert(error.retry_after)
            embed = discord.Embed(title = f"Cooldown", description = str(msg), color = ctx.author.colour)
            embed.set_author(name = ctx.author.display_name, icon_url = ctx.author.avatar_url)
            await ctx.reply(embed = embed ,delete_after = 10,ephemeral=True)
            await ctx.message.delete()
        else:
            raise error

    @client.hybrid_command(name = "stats",description="Stats",with_app_command = True)
    async def stats(self, ctx):
 

        serverCount = len(self.client.guilds)
        memberCount = len(set(self.client.get_all_members()))


        # other stuff
        currentTime = int(time.time())

        embed = discord.Embed(title=f'{self.client.user.name} - Stats ',
                              colour=ctx.author.colour,
                              timestamp=ctx.message.created_at)


        embed.add_field(name='Bot stats',
                        value=f'ID: {self.client.user.id}\n'
                              f'🏘️ Servers: {serverCount:,}\n'
                              f'👥 Total members: {memberCount:,}')

        await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
    await client.add_cog(misc(client))