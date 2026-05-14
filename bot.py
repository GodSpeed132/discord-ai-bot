import discord
from discord.ext import commands
from dotenv import load_dotenv 
import os
from cogs.convo import convo


load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')  #discord token goes here


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

async def loadcog():
    try:
        await bot.add_cog(convo(bot))
    except Exception as e:
        print(f"Error: {e}")

bot.setup_hook = loadcog

bot.run(DISCORD_TOKEN)