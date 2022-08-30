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

pre1 = get_prefix
pre = pre1

embed = discord.Embed(title = " Overlord ", description = "**```Interact with the menu below for further help.```\n```All the commands in this help menu supports slash commands.```**")

embed2 = discord.Embed(title = "🛠️ | Moderation", description = "**`clear` `kick` `ban` `unban` **")
embed2.add_field(name="Requirement", value="**```Administrator Permissions ```**", inline = False)
embed2.add_field(name=f"**[bot_prefix]clear**", value=f"**```[bot_prefix]clear <number of messages> | clears message```**")
embed2.add_field(name=f"**[bot_prefix]kick**", value=f"**```[bot_prefix]kick [member] | Kicks a member from the server```**")
embed2.add_field(name=f"**[bot_prefix]ban**", value=f"**```[bot_prefix]ban [member] | Bans a member from the server```**")
embed2.add_field(name=f"**[bot_prefix]unban**", value=f"**```[bot_prefix]unban [member_id] | UnBans a member in the server```**")

embed3 = discord.Embed(title = "⚽ | Fun", description = "**`8ball` `tictactoe` `topic` `kill` `roast` `coffee` `beer` `meme` `cat` `dog` `fox`**")
embed3.add_field(name="Requirement", value="**```None ```**", inline = False)
embed3.add_field(name=f"**[bot_prefix]8ball**", value=f"**```[bot_prefix]8ball <question>```**")
embed3.add_field(name=f"**[bot_prefix]tictactoe**", value=f"**```[bot_prefix]tictactoe [member1] [member2]```**")
embed3.add_field(name=f"**[bot_prefix]topic**", value=f"**```[bot_prefix]topic | Random topics```**")
embed3.add_field(name=f"**[bot_prefix]attack**", value=f"**```[bot_prefix]attack [member] | A fun kill command ```**")
embed3.add_field(name=f"**[bot_prefix]roast**", value=f"**```[bot_prefix]roast [member] | Roast your friends```**")
embed3.add_field(name=f"**[bot_prefix]coffee**", value=f"**```[bot_prefix]coffee [member] | Share a cup of coffee```**")
embed3.add_field(name=f"**[bot_prefix]beer**", value=f"**```[bot_prefix]beer [member] | Have a beer party with your friend```**")
#embed3.add_field(name=f"**[bot_prefix]meme**", value="**```[bot_prefix]meme | Top memes from reddit```**")
#embed3.add_field(name=f"**[bot_prefix]cat**", value="**```[bot_prefix]cat | Random cat images ```**")
#embed3.add_field(name="**[bot_prefix]dog**", value="**```[bot_prefix]dog | Random dog images```**")
#embed3.add_field(name="**[bot_prefix]fox**", value="**```[bot_prefix]fox| Random fox images```**")

embed4 = discord.Embed(title = "💸 | Economy", description = "**`shop` `buy` `sell` `inventory` `balance` `withdraw` `deposit` `transfer` `rob` `viewbalance` `viewinventory` `daily` `beg` `slots` `work` `fish` `hunt`**")
embed4.add_field(name="Requirement", value="**``` None ```**", inline = False)
embed4.add_field(name=f"**[bot_prefix]shop**", value="**```[bot_prefix]shop to see list of buyable things```**")
embed4.add_field(name=f"**[bot_prefix]buy**", value="**```[bot_prefix]buy [itemid] [amount] | Amount is optional```**")
embed4.add_field(name=f"**[bot_prefix]sell**", value="**```[bot_prefix]sell [itemid] [amount] | Amount is optional```**")
embed4.add_field(name=f"**[bot_prefix]bag [member](optional)**", value="**```[bot_prefix]inventory or [bot_prefix]bag or [bot_prefix]inv | To view your inventory```**")
embed4.add_field(name=f"**[bot_prefix]balance [member](optional)**", value=f"**```[bot_prefix]balance or [bot_prefix]bal | To view your balance```**")
embed4.add_field(name=f"**[bot_prefix]withdraw**", value=f"**```[bot_prefix]withdraw [amount] | Withdraw money from your bank```**")
embed4.add_field(name=f"**[bot_prefix]deposit**", value=f"**```[bot_prefix]Deposit [amount] | Deposit money to your bank```**")
embed4.add_field(name=f"**[bot_prefix]transfer**", value=f"**```[bot_prefix]transfer [member] [amount] | Transfer money from your bank to another```**")
embed4.add_field(name=f"**[bot_prefix]rob**", value=f"**```[bot_prefix]rob [member] | Rob from a member's wallet.```**")
embed4.add_field(name=f"**[bot_prefix]daily**", value=f"**```[bot_prefix]daily | Collect your daily coins```**")
embed4.add_field(name=f"**[bot_prefix]beg**", value=f"**```[bot_prefix]beg | Beg for coins ```**")
embed4.add_field(name=f"**[bot_prefix]slots**", value=f"**```[bot_prefix]slots [amount] | Bet your coins and test your luck```**")
embed4.add_field(name=f"**[bot_prefix]work**", value=f"**```[bot_prefix]work| Work every hour to earn coins```**")
embed4.add_field(name=f"**[bot_prefix]fish**", value=f"**```[bot_prefix]fish | Fish to catch fishes and collect or sell them for coins```**")
embed4.add_field(name=f"**[bot_prefix]hunt**", value=f"**```[bot_prefix]hunt | Hunt to catch animals and collect or sell them for coins```**")

embed5 = discord.Embed(title = "🎉 | Giveaway", description = "**`giveaway` `reroll`**")
embed5.add_field(name="Requirement", value="**```Role: Giveaway Manager```**", inline = False)
embed5.add_field(name="**[bot_prefix]giveaway**", value="**```[bot_prefix]giveaway | To begin the giveaway setup```**")
embed5.add_field(name="**[bot_prefix]reroll**", value="**```[bot_prefix]reroll [channel] [no.of winners] | Reroll a giveaway winner```**")
embed5.add_field(name="**[bot_prefix]gend**", value="**```[bot_prefix]gend [message_id] [no.of winners] | End giveaway```**")
embed5.add_field(name="**[bot_prefix]gclose**", value="**```[bot_prefix]gclose [channel] [message_id]  [no.of winners] |In case [bot_prefix]reroll and [bot_prefix]gend doesn't work.```**")

embed6 = discord.Embed(title = "📁 | General", description = "**`define` `dailyfacts` `roll` `coin`**")
embed6.add_field(name="Requirement", value="**``` None ```**", inline = False)
embed6.add_field(name="**[bot_prefix]roll**", value="**```[bot_prefix]dice | Roll a random number between 0 - 101```**")
embed6.add_field(name="**[bot_prefix]coin**", value="**```[bot_prefix]coin | Head or Tails```**")
embed6.add_field(name="**[bot_prefix]define**", value="**```[bot_prefix]define <word> | Get definition for a word```**")
embed6.add_field(name="**[bot_prefix]dailyfact**", value="**```[bot_prefix]dailyfact | Gives a new fact each day```**")
embed6.add_field(name="**[bot_prefix]helplang**", value="**```[bot_prefix]helplang | List of languages for [bot_prefix]tlate cmd```**")
embed6.add_field(name="**[bot_prefix]dtect**", value="**```[bot_prefix]dtect word/sentence | Detects the source language```**")
embed6.add_field(name="**[bot_prefix]t**", value="**```[bot_prefix]t <to_language> word | Get translation for a word/sentence | Aliases = [bot_prefix]translate or [bot_prefix]tlate```**")

embed7 = discord.Embed(title = "📌 | Utility", description = "**`serverinfo` `userinfo` `afk` `poll`**")
embed7.add_field(name="Requirement", value="**``` None ```**", inline = False)        
embed7.add_field(name=f"**[bot_prefix]serverinfo**", value=f"**```[bot_prefix]serverinfo | Info of the current server```**")
embed7.add_field(name=f"**[bot_prefix]userinfo**", value=f"**```[bot_prefix]userinfo <@user> | Gives info about an user```**")
embed7.add_field(name=f"**[bot_prefix]avatar**", value=f"**```[bot_prefix]avatar <@user>(optional)  | Gives the avatar of the user```**")       
embed7.add_field(name=f"**[bot_prefix]poll**", value=f"""**```[bot_prefix]poll "[question]" "[choice1]" "[choice2]" | Maximum of 20 choices. "" Is mandatory```**""")
embed7.add_field(name=f"**[bot_prefix]afk**", value=f"**```[bot_prefix]afk <reason>(optional) | Sets afk.```**")

embed8 = discord.Embed(title = "💠 | Misc", description = "**`ping` `setprefix`**")
embed8.add_field(name="Requirement", value="**``` None ```**", inline = False)
embed8.add_field(name="[bot_prefix]ping", value="**```[bot_prefix]ping | Find the bot latency```**")
embed8.add_field(name="prefix", value="**```@Overlord (mention the bot) | Find the bot prefix in this server```**")
embed8.add_field(name="[bot_prefix]setprefix", value="**```[bot_prefix]setprefix <newprefix> | Set custom prefix for the bot in this server. Note : Need admin```**")

embed11 = discord.Embed(title = "🤗 | Actions", description = "**`highfive` `slap` `greet` `kill` `hug`**")
embed11.add_field(name="Requirement", value="** None **", inline = False)
embed11.add_field(name=f"`[bot_prefix]highfive`", value=f"**```[bot_prefix]highfive [member]```**")
embed11.add_field(name=f"`[bot_prefix]slap`", value=f"**```[bot_prefix]slap [member]```**")
embed11.add_field(name=f"`[bot_prefix]greet`", value=f"**```[bot_prefix]greet [member]```**")
embed11.add_field(name=f"`[bot_prefix]kill`", value=f"**```[bot_prefix]kill [member]``` **")
embed11.add_field(name=f"`[bot_prefix]hug`", value=f"**```[bot_prefix]hug [member]```**")        

embed9 = discord.Embed(title = "🔗 | Invite Link",url ="https://discord.com/api/oauth2/authorize[bot_prefix]client_id=860755400290992179&permissions=8&scope=bot")

class Select(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Moderation",emoji="🛠️",description="This is option 1!"),
            discord.SelectOption(label="Fun",emoji="⚽",description="This is option 2!"),
            discord.SelectOption(label="Economy",emoji="💸",description="This is option 3!"),
            discord.SelectOption(label="Utility",emoji="📌",description="This is option 3!"),
            discord.SelectOption(label="Actions",emoji="🤗",description="This is option 3!"),
            discord.SelectOption(label="Support",emoji="🔗",description="This is option 3!")
            #discord.SelectOption(label="Option 3",emoji="🎭",description="This is option 3!")
            ]
        super().__init__(placeholder="Select an option",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Moderation":
            await interaction.response.edit_message(embed=embed2,ephemeral=True)
        elif self.values[0] == "Fun":
            await interaction.response.send_message(embed=embed3,ephemeral=True)
        elif self.values[0] == "Economy":
            await interaction.response.send_message(embed=embed4,ephemeral=True)
        elif self.values[0] == "Utility":
            await interaction.response.send_message(embed=embed7,ephemeral=True)
        elif self.values[0] == "Actions":
            await interaction.response.send_message(embed=embed11,ephemeral=True)
        elif self.values[0] == "Support":
            await interaction.response.send_message(embed=embed9,ephemeral=True)

class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Select())

@client.hybrid_command(name = "helpmenu", description="Help Menu",with_app_command = True)
async def helpmenu(ctx):
    await ctx.send(embed=embed,view=SelectView(),ephemeral=True)

async def setup(client):
   client.add_command(helpmenu)