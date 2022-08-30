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

@client.hybrid_command(name = "balance", description="Check your balance",with_app_command = True)
@commands.cooldown(1,3,commands.BucketType.user)
async def balance(ctx,*,member:discord.Member = None):
    if member == None:
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

@client.hybrid_command(name = "withdraw", description="Withdraw from your bank",with_app_command = True)
@commands.cooldown(1,3,commands.BucketType.user)
async def withdraw(ctx,amount =None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.reply("Please enter the amount")
        return
    
    bal = await update_bank(ctx.author)
    if amount == "all":
         amount = bal[1]
    if amount == "max":
      amount = bal[1]

    amount = int(amount)
    if amount>bal[1]:
        await ctx.reply("You don't have that much money in your bank!")
        return
    if amount<0:
        await ctx.reply("Amount must be positive")
        return
    
    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,"bank")
    
    await ctx.reply(f"You withdrew **Ⓥ** {amount} coins!")

@client.hybrid_command(name = "deposit", description="Deposit from wallet to your bank",with_app_command = True)
@commands.cooldown(1,3,commands.BucketType.user)
async def deposit(ctx,amount =None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.reply("Please enter the amount")
        return
    
    bal = await update_bank(ctx.author)
    if amount == "all":
         amount = bal[0]
    if amount == "max":
      amount = bal[0]

    amount = int(amount)
    if amount>bal[0]:
        await ctx.reply("You don't have that much money in your wallet!")
        return
    if amount<0:
        await ctx.reply("Amount must be positive")
        return
    
    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,"bank")
    
    await ctx.reply(f"You deposited **Ⓥ** {amount} coins!")

@client.hybrid_command(name = "transfer", description="Transfer money from your bank to a user's bank",with_app_command = True)
@commands.cooldown(1,3,commands.BucketType.user)
async def transfer(ctx,member:discord.Member,amount = None):
    await open_account(ctx.author)
    await open_account(member)

    if amount == None:
        await ctx.reply("Please enter the amount")
        return
       
    bal = await update_bank(ctx.author)
    if amount == "all":
         amount = bal[1]
    if amount == "max":
      amount = bal[1]

    amount = int(amount)
    if amount>bal[1]:
        await ctx.reply("You don't have that much money in your bank!")
        return
    if amount<0:
        await ctx.reply("Amount must be positive")
        return
    
    await update_bank(ctx.author,-1*amount,"bank")
    await update_bank(member,amount,"bank")
    
    await ctx.reply(f"You transferred **Ⓥ** {amount} coins to {member}'s bank!")

@client.hybrid_command(name = "give", description="Give a user money from your wallet",with_app_command = True)
@commands.cooldown(1,3,commands.BucketType.user)
async def give(ctx,member:discord.Member,amount = None):
    await open_account(ctx.author)
    await open_account(member)

    if amount == None:
        await ctx.reply("Please enter the amount")
        return
    
    bal = await update_bank(ctx.author)
    if amount == "all":
         amount = bal[0]
    if amount == "max":
      amount = bal[0]

    amount = int(amount)
    if amount>bal[0]:
        await ctx.reply("You don't have that much money in your wallet!")
        return
    if amount<0:
        await ctx.reply("Amount must be positive")
        return
    
    await update_bank(ctx.author,-1*amount,"wallet")
    await update_bank(member,amount,"wallet")
    
    await ctx.reply(f"You gave **Ⓥ** {amount} coins to {member}'s wallet!")

async def setup(client):
    client.add_command(balance)
    client.add_command(give)
    client.add_command(transfer)
    client.add_command(deposit)
    client.add_command(withdraw)