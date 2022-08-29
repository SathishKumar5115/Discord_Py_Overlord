import discord
from discord.ext import commands
import json

def get_prefix(client, message):

  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)

  return prefixes[str(message.guild.id)]

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = get_prefix, case_insensitive = True, intents=intents,allowed_mentions = discord.AllowedMentions(everyone = bool))

async def open_account(user):
    
    users = await get_bank_data()
    
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0
        users[str(user.id)]["bag"] = []

    with open("mainbank.json","w") as f:
        json.dump(users,f)
    return True

async def get_bank_data():
    with open("mainbank.json","r") as f:
        users = json.load(f)

    return users

async def update_bank(user,change = 0,mode = "wallet"):
    users = await get_bank_data()
 
    users[str(user.id)][mode] += change

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
    return bal

@commands.command(aliases=["bal"])
@commands.cooldown(1,3,commands.BucketType.user)
async def balance(ctx,*,member:discord.Member = ""):
    if member == "":
        await open_account(ctx.author)
        user = ctx.author

        users = await get_bank_data()

        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]

        em = discord.Embed(title = f"💰 {ctx.author.name}'s balance 💰")

        em.add_field(name = "| Wallet Balance |",value = f"**Ⓥ**  {wallet_amt}",inline=False)
        em.add_field(name = "| Bank Balance |",value = f"**Ⓥ**  {bank_amt}",inline=False)
        msg = 'You need to mention a user.'
        await ctx.reply(embed = em)
        return
    else:
        await open_account(member)
        user = member
        users = await get_bank_data()
        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]
        em = discord.Embed(title = f"💰 {member.name}'s balance 💰")
        em.add_field(name = f"| Wallet Balance |",value = f"**Ⓥ** {wallet_amt}",inline=False)
        em.add_field(name = f"| Bank Balance |" ,value = f"**Ⓥ** {bank_amt}",inline=False)
        await ctx.reply(embed = em)

async def setup(client):
     client.add_command(balance)