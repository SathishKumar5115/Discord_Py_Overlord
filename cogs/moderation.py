import discord
from discord.ext import commands
import json
import datetime

def get_prefix(client, message):

  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)

  return prefixes[str(message.guild.id)]

intents = discord.Intents.default() 
intents.members = True
client = commands.Bot(command_prefix = get_prefix, case_insensitive = True, intents=intents)


class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @client.hybrid_command(name = "purge",description="Purge messages",with_app_command = True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=1):
      await ctx.message.delete()
      await ctx.channel.purge(limit=amount)
      embed2 = discord.Embed(title="<a:checked:873119975219539979> Chat Purged", description=f"**{ctx.author.mention} purged {amount} messages **", colour=ctx.author.color, timestamp=datetime.datetime.utcnow())
      embed2.set_thumbnail(url = ctx.guild.icon.url)
      await ctx.send(embed=embed2)

    @client.hybrid_command(name = "kick",description="Kick a user",with_app_command = True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : commands.MemberConverter, *,reason=None):
      await member.kick(reason=reason)
      embed2 = discord.Embed(title="<a:checked:873119975219539979>  Member Kicked", description=f"**Kicked {member} \n\n Reason: {reason}**", colour=ctx.author.color, timestamp=datetime.datetime.utcnow())
      embed2.set_thumbnail(url = member.avatar.url)
      embed2.set_footer(text=ctx.author.name,icon_url=ctx.author.avatar.url)
      #await ctx.message.add_reaction('<a:checked:873119975219539979>')
      await ctx.send(embed=embed2)
      embed = discord.Embed(title="Kicked", description=f"**You are kicked from: {ctx.guild.name}\n\n Reason: {reason}.**", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
      embed.set_thumbnail(url = ctx.guild.icon.url)     
      await member.send(embed=embed)

    @client.hybrid_command(name = "ban",description="Ban a user",with_app_command = True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx,member: discord.Member, *, reason=None):
      await member.ban(reason=reason)
      embed2 = discord.Embed(title="<a:checked:873119975219539979>  Member Banned", description=f"**Banned {member} \n\n Reason: {reason}**", colour=ctx.author.color, timestamp=datetime.datetime.utcnow())
      embed2.set_thumbnail(url = member.avatar.url)
      embed2.set_footer(text=ctx.author.name,icon_url=ctx.author.avatar.url)
      #await ctx.message.add_reaction('<a:checked:873119975219539979>')
      await ctx.send(embed=embed2)
      embed = discord.Embed(title="Banned", description=f"**You are banned from: {ctx.guild.name}\n\n Reason: {reason}.**", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
      embed.set_thumbnail(url = ctx.guild.icon.url)     
      await member.send(embed=embed)

    @client.hybrid_command(name = "unban",description="Unban a user",with_app_command = True)
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def unban(self, ctx, user: discord.User):
      invite = await ctx.channel.create_invite()
      if user == None:
        embed = discord.Embed(f"{ctx.message.author}, Please enter a valid user!")
        await ctx.reply(embed=embed)

      else:
        guild = ctx.guild
        await guild.unban(user=user)
        embed2 = discord.Embed(title="<a:checked:873119975219539979>  Member UnBanned", description=f"**UnBanned {user}**", colour=ctx.author.color, timestamp=datetime.datetime.utcnow())
        embed2.set_thumbnail(url = user.avatar.url)
        embed2.set_footer(text=ctx.author.name,icon_url=ctx.author.avatar.url)
        #await ctx.message.add_reaction('<a:checked:873119975219539979>')
        await ctx.send(embed=embed2)
        embed = discord.Embed(title="UnBanned", description=f"**You are Unbanned in: {ctx.guild.name}.**\n\n {invite}", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url = ctx.guild.icon.url)     
        await user.send(embed=embed)
        

    @client.hybrid_command(name = "mute",description="Mute a user",with_app_command = True)
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        #await ctx.message.add_reaction('<a:loading:872694349899632670>')
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")
            return

        for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True)

        embed = discord.Embed(title="<a:checked:873119975219539979>  Muted", description=f"{member.mention} was muted ", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Reason:", value=reason, inline=False)
        embed.set_thumbnail(url = member.avatar.url)
        await ctx.reply(embed=embed)
        await member.add_roles(mutedRole, reason=reason)
        embed2 = discord.Embed(title="Muted", description=f"**You are muted in: {guild.name}\n \nReason:{reason}**", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
        embed2.set_thumbnail(url = ctx.guild.icon.url)
        #await ctx.message.clear_reaction('<a:loading:872694349899632670>')
        #await ctx.message.add_reaction('<a:checked:873119975219539979>')
        await member.send(embed=embed2)


    @client.hybrid_command(name = "unmute",description="Unmute a user",with_app_command = True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

        await member.remove_roles(mutedRole)
        embed2 = discord.Embed(title="<a:checked:873119975219539979>  UnMuted", description=f"**You are unmuted in: {ctx.guild.name}.**", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
        embed2.set_thumbnail(url = ctx.guild.icon.url)
        #await ctx.message.clear_reaction('<a:loading:872694349899632670>')
        #await ctx.message.add_reaction('<a:checked:873119975219539979>')
        await member.send(embed=embed2)
        embed = discord.Embed(title="Unmute", description=f"Unmuted {member.mention}", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url = member.avatar.url)
        await ctx.reply(embed=embed)


async def setup(client):
  await client.add_cog(Moderation(client)) 