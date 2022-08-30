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

embed = discord.Embed(title = "Overlord", description = "**```Welcome to Void Shop. Interact with the buttons below.```**")

embed9 = discord.Embed(title = "🏬 | Main shop", description = "**Welcome to the main shop**")
embed9.add_field(name = ":cookie: | Cookie | **Ⓥ** 10", value = f"**```Cookie \nID = cookie```**")
embed9.add_field(name = ":beer: | Alcohol | **Ⓥ** 100", value = f"**```Down some alcohol \nID = alcohol```**")
embed9.add_field(name = ":pizza: | Pizza Slice | **Ⓥ** 200", value = "**```Pizza time \nID = pizzaslice ```**")
embed9.add_field(name = ":coin: | Void Coin | **Ⓥ** 7000", value = " **```A pretty rare coin, probably only fairly rich people have this! \nID = voidcoin```**")
embed9.add_field(name = ":first_place: | Void Medal | **Ⓥ** 15000", value = "**```A medal only the top 5 percent of players have! \nID = voidmedal```**")
embed9.add_field(name = ":trophy: | Void Trophy | **Ⓥ** 20000 ", value = "**```A trophy to flex how rich you are! You are rich enough to afford this... right? \nID = voidtrophy```**",inline = False)
embed9.add_field(name = ":crown: | Void Crown | **Ⓥ** 50000 ", value = "**```Literally only the richest of the richest of the richest of the richest of the richest of the rich will hold these beloved crowns. \nID = voidcrown```**")

embed10 = discord.Embed(title = "🎣 | Fish shop", description = "**Fish using the ?fish command**")
embed10.add_field(name = ":fish: | Fish **Ⓥ** 10", value = f"**```ID = fish```**")
embed10.add_field(name = ":tropical_fish: | Tropical Fish | **Ⓥ** 25", value = f"**```ID = tropicalfish```**")
embed10.add_field(name = ":blowfish: | Blow Fish | **Ⓥ** 50", value = "**```ID = blowfish ```**")
embed10.add_field(name = ":octopus: | Octopus | **Ⓥ** 100", value = " **```ID = octopus```**")
embed10.add_field(name = ":squid: | Squid | **Ⓥ** 250", value = "**```ID = squid```**")
embed10.add_field(name = ":dolphin: | Dolphin | **Ⓥ** 500 ", value = "**```ID = dolphin```**")
embed10.add_field(name = ":crocodile: | Crocodile | **Ⓥ** 750 ", value = "**```ID = crocodile```**")
embed10.add_field(name = ":shark: | Shark | **Ⓥ** 1400 ", value = "**```ID = shark```**")
embed10.add_field(name = ":whale: | Whale | **Ⓥ** 2000 ", value = "**```ID = whale```**")

embed11 = discord.Embed(title = "🐵 | Animal shop", description = "**Hunt using the ?hunt command**")
embed11.add_field(name = ":rabbit: | Rabbit **Ⓥ** 100", value = f"**```ID = rabbit```**")
embed11.add_field(name = ":duck: | Duck | **Ⓥ** 100", value = f"**```ID = duck```**")
embed11.add_field(name = ":boar: | Boar | **Ⓥ** 200", value = "**```ID = boar ```**")
embed11.add_field(name = ":deer: | Deer | **Ⓥ** 300", value = " **```ID = deer```**")
embed11.add_field(name = ":tiger2: | Tiger | **Ⓥ** 500", value = "**```ID = tiger```**")
embed11.add_field(name = ":lion: | Lion | **Ⓥ** 700 ", value = "**```ID = lion```**")
embed11.add_field(name = ":rhino: | Rhino | **Ⓥ** 500 ", value = "**```ID = rhino```**")
embed11.add_field(name = ":unicorn: | Unicorn | **Ⓥ** 2500 ", value = "**```ID = unicorn```**")
embed11.add_field(name = ":dragon: | Dragon | **Ⓥ** 2500 ", value = "**```ID = dragon```**")

class Buttons(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="Hunter's Shop",style=discord.ButtonStyle.green, custom_id = "hunter")
    async def hunet_button(self,interaction:discord.Interaction,button:discord.ui.Button):
        await interaction.response.edit_message(embed=embed11)
    @discord.ui.button(label="Fisher's Shop",style=discord.ButtonStyle.gray)
    async def fisher_button(self,interaction:discord.Interaction,button:discord.ui.Button):
        await interaction.response.edit_message(embed=embed10)
    @discord.ui.button(label="Main Shop",style=discord.ButtonStyle.red)
    async def main_button(self,interaction:discord.Interaction,button:discord.ui.Button):
        await interaction.response.edit_message(embed=embed9)  

@client.hybrid_command(name = "shop", description="Check Out the Shop",with_app_command = True)
async def shopmenu(ctx):
    view=Buttons()
    await ctx.reply(embed=embed,view=view)

async def setup(client):
   client.add_command(shopmenu)