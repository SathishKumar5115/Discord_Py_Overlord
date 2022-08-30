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

mainshop = [{"name":"cookie","price":10},
            {"name":"Alcohol","price":100},
            {"name":"PizzaSlice","price":200},
            {"name":"VoidCoin","price":7000},
            {"name":"VoidMedal","price":15000},
            {"name":"VoidTrophy","price":20000},
            {"name":"VoidCrown","price":50000},
            {"name":"fish","price":10},
            {"name":"tropicalfish","price":25},
            {"name":"blowfish","price":50},
            {"name":"octopus","price":100},
            {"name":"squid","price":250},
            {"name":"dolphin","price":500},
            {"name":"shark","price":1400},
            {"name":"crocodile","price":750},
            {"name":"whale","price":2000},
            {"name":"rabbit","price":100},
            {"name":"duck","price":100},
            {"name":"boar","price":200},
            {"name":"deer","price":300},
            {"name":"tiger","price":500},
            {"name":"lion","price":700},
            {"name":"rhino","price":500},
            {"name":"unicorn","price":2500},
            {"name":"dragon","price":2500},]

   
corresponding = {'cookie':":cookie:", 'alcohol':":beer:", 'pizzaslice':":pizza:", 'voidcoin':":coin:", 'voidmedal':":first_place:", 'voidtrophy':":trophy:", 'voidcrown':":crown:",'fish':":fish:",'tropicalfish':":tropical_fish:",'blowfish':":blowfish:",'octopus':":octopus:",'squid':":squid:",'dolphin':":dolphin:", 'shark':":shark:",'rhinoceros':":rhino:",'crocodile':":crocodile:",'whale':":whale:",'rabbit':":rabbit:",'duck':":duck:",'boar':":boar:",'deer':":deer:",'tiger':":tiger2:",'lion':":lion:",'rhino':":rhino:",'unicorn':":unicorn:",'dragon':":dragon:"}

@client.hybrid_command(name = "fish", description="Fishing",with_app_command = True)
@commands.cooldown(1,10,commands.BucketType.user)
async def fish(ctx):
    await money.open_account(ctx.author)
    users = await money.get_bank_data()
    user = ctx.author
    fishes = ['fish','tropicalfish','','blowfish','','crocodile','','octopus','','squid','dolphin','shark','whale']


    fishc = random.choice(fishes)
    amount = random.randint(1,5)
    if fishc == "":
        return await ctx.reply(f"You went Fishing and found Nothing ")
      
    await ctx.reply(f"You cast out your line and brought back {amount} {corresponding[fishc]} {fishc.title()} !!")
    
    for i in users[str(user.id)]["bag"]:
        if fishc in i.values():
            i['amount']+=amount
            with open("mainbank.json", "w") as f:
                json.dump(users, f)
            return
       
    else:
        users[str(user.id)]["bag"].append({"item": fishc, "amount": amount}) 
        with open("mainbank.json", "w") as f:
            json.dump(users, f)
        return

@client.hybrid_command(name = "hunt", description="Hunt in the forest",with_app_command = True)
@commands.cooldown(1,10,commands.BucketType.user)
async def hunt(ctx):
    await money.open_account(ctx.author)
    users = await money.get_bank_data()
    user = ctx.author
    hunts = ['rabbit','','duck','','boar','deer','','tiger','','lion','','rhino','','unicorn','dragon']


    huntc = random.choice(hunts)
    amount = random.randint(1,5)
    if huntc == "":
        return await ctx.reply(f"You went hunting but found Nothing ")
      
    await ctx.reply(f"You went hunting in the woods and brought back {amount} {corresponding[huntc]} {huntc.title()} !!")
    
    for i in users[str(user.id)]["bag"]:
        if huntc in i.values():
            i['amount']+=amount
            with open("mainbank.json", "w") as f:
                json.dump(users, f)
            return
       
    else:
        users[str(user.id)]["bag"].append({"item": huntc, "amount": amount}) 
        with open("mainbank.json", "w") as f:
            json.dump(users, f)
        return


@client.hybrid_command(name = "buy", description="Buy an item from shop",with_app_command = True)
@commands.cooldown(1,3,commands.BucketType.user)
async def buy(ctx,item,amount = 1):
    await money.open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
            return


    await ctx.send(f"You just bought {amount} {item}")

@client.hybrid_command(name = "sell", description="Sell and item to the shop",with_app_command = True)
@commands.cooldown(1,3,commands.BucketType.user)
async def sell(ctx,item,amount = 1):
    await money.open_account(ctx.author)

    res = await sell_this(ctx.author,item,amount)
    users = await money.get_bank_data()
    


    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have {amount} {item} in your bag.")
            return
        if res[1]==3:
            await ctx.send(f"You don't have {item} in your bag.")
            return

    await ctx.reply(f"You just sold {amount} {item}.")

async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 1* item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await money.get_bank_data()

    bal = await money.update_bank(user)


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return [False,3]
    except:
        return [False,3]    

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await money.update_bank(user,cost,"wallet")

    return [True,"Worked"]

async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await money.get_bank_data()

    bal = await money.update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["bag"] = [obj]        

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await money.update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]

@client.hybrid_command(name = "inventory", description="Check a users' or your inventory",with_app_command = True)
@commands.cooldown(1,3,commands.BucketType.user)
async def bag(ctx,*,member:discord.Member=None):
  if member == None:
    await money.open_account(ctx.author)
    user = ctx.author
    users = await money.get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []
    
    em = discord.Embed(title = f"{ctx.author}'s Bag")
    for item in bag:
        name = item["item"]
        amount = item["amount"]
        if amount==0:
            continue
        else:
            em.add_field(name = f"{corresponding[name]} | {name}  : {amount}", value = f"```ID = {name}```")

    await ctx.reply(embed = em)
    return
  await money.open_account(member)
  user = member
  users = await money.get_bank_data()

  try:
      bag = users[str(user.id)]["bag"]
  except:
      bag = []


  em = discord.Embed(title = f"{member}'s Bag")
  for item in bag:
      name = item["item"]
      amount = item["amount"]
      if amount==0:
         continue
      else:
          em.add_field(name = f"{corresponding[name]} | {name}  : {amount}", value = f"```ID = {name}```")

  await ctx.reply(embed = em)

async def setup(client):
    client.add_command(bag)
    client.add_command(sell)
    client.add_command(buy)
    client.add_command(hunt)
    client.add_command(fish)
