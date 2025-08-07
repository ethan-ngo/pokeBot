import discord
from discord.ext import commands
from discord.ui import Button, View
from dotenv import load_dotenv
import os
from checkStock import addFromPage

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Your item queue or stock-checker could call this:
async def send_stock_alert(tcin):
    channel = bot.get_channel(CHANNEL_ID)
    
    class ConfirmView(View):
        @discord.ui.button(label="✅ Approve", style=discord.ButtonStyle.success)
        async def approve(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.send_message(f"Item {tcin} approved ✅")
            addFromPage(tcin, EMAIL, PASSWORD)

        @discord.ui.button(label="❌ Ignore", style=discord.ButtonStyle.danger)
        async def deny(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.send_message(f"Ignored item {tcin} ❌")

    await channel.send(
        f"🎯 Item {tcin} is in stock! Approve to add to cart:",
        view=ConfirmView()
    )

def add_to_cart(tcin):
    print(f"Adding item {tcin} to cart...")
    # Call your selenium function here

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    # You can even trigger a test alert here
    await send_stock_alert("1003167760")

bot.run(TOKEN)