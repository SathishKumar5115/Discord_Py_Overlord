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

@client.hybrid_command(name = "beg",description="Beg for some coins",with_app_command = True)
@commands.cooldown(1,10,commands.BucketType.user)
async def beg(ctx):
    await money.open_account(ctx.author)

    users = await money.get_bank_data()

    user = ctx.author

    earnings = random.randrange(200)

    people = ['Not Jonam','Shark','Sid','Mr.Beast','Minecraft Steve','Overlord','Pewdiepie','God','Tharthegamer']

    bruh = random.choice(people)

    responses = [f'Oh you poor little beggar, take **Ⓥ** {earnings}.',
                     'No I already gave money to the last beggar.',
                     'honestly why are you even begging, get a job.',
                     f'{bruh} gave you **Ⓥ** {earnings}.',
                     f'{bruh} dropped **Ⓥ** {earnings}.'
                     ]
    
    
    
    embed = discord.Embed(description = f"{random.choice(responses)}",color = ctx.author.color)
    await ctx.reply(embed=embed)

    users[str(user.id)]["wallet"] += earnings 

    with open("mainbank.json","w") as f:
        json.dump(users,f)

@client.hybrid_command(name = "work",description="Work Hard",with_app_command = True)
@commands.cooldown(1,3600,commands.BucketType.user)
async def work(ctx):
    await money.open_account(ctx.author)

    users = await money.get_bank_data()

    user = ctx.author

    earnings = random.randint(500,1500)
    wallet_amt = users[str(user.id)]["wallet"]

    em = discord.Embed(title ="Work Results : ",description = f"{ctx.author.mention} has Earned **Ⓥ**       {earnings} coins through working !!")
    em.set_thumbnail(url="https://media.discordapp.net/attachments/855799829866348544/860880807254163486/pengwork.gif")
  
    await ctx.reply(embed = em)

    users[str(user.id)]["wallet"] += earnings 

    with open("mainbank.json","w") as f:
        json.dump(users,f)

@client.hybrid_command(name = "daily",description="Daily Coins",with_app_command = True)
@commands.cooldown(1,86400,commands.BucketType.user)
async def daily(ctx,amount = 1500):
    await money.open_account(ctx.author)

    await money.update_bank(ctx.author,amount)
    em = discord.Embed(title ="Daily Coins",description = f"You claimed your daily **Ⓥ** 1500 coins!")
    await ctx.reply(embed=em)

@client.hybrid_command(name = "slots",description="Test your luck",with_app_command = True)
@commands.cooldown(1,3,commands.BucketType.user)
async def slots(ctx,amount = None):
    await money.open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return
    
    bal = await money.update_bank(ctx.author)

    amount = int(amount)
    if amount>bal[0]:
        await ctx.reply("You don't have that much money in your wallet!")
        return
    if amount<0:
        await ctx.reply("Amount must be positive")
        return
 
    final = [] 
    for i in range(3):
        a = random.choice(["🤑","🪙","💰"])

        final.append(a)

    if final[1] == final[2] == final[0]:
        await money.update_bank(ctx.author,2*amount)
        em = discord.Embed(title = "   ".join(final) , description = f"You Won\n{ctx.author.mention} have got **Ⓥ**{amount}x2 credits By Slots :)",color = ctx.author.colour)
    else:
        await money.update_bank(ctx.author,-1*amount)
        em = discord.Embed(title = "   ".join(final) , description = f"{ctx.author.mention} have Lost **Ⓥ**{amount} credits \nBetter luck Next time :(",color = ctx.author.colour)
    em.set_thumbnail(url = ctx.author.avatar.url)
    await ctx.reply(embed = em)

@client.hybrid_command(name = "leaderboard",description="Are you one of the richest?",with_app_command = True)
async def leaderboard(ctx,x = 5):
    users = await money.get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total,reverse=True)    

    em = discord.Embed(title = f"Top {x} Richest People" , description = "This is decided on the basis of raw money in the bank and wallet",color = ctx.author.color)
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = client.get_user(id_)
        name = member.name
        em.add_field(name = f"{index}. {name}" , value = f"{amt}",  inline = False)
        if index == x:
            break
        else:
            index += 1

    await ctx.reply(embed = em)

async def setup(client):
    client.add_command(beg)
    client.add_command(work)
    client.add_command(daily)
    client.add_command(slots)
    client.add_command(leaderboard)