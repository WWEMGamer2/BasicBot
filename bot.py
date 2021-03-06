import discord
import os
from functionalities import Actions, Events, Main
from discord.ext import commands
bot = commands.Bot(command_prefix="COMMAND_PREFIX_HERE")

@bot.event
async def on_connect():
  print("Starting setup...")
  
# COMMANDS:

@bot.command()
async def test(ctx):
  print(f"test command executed from {ctx.guild}")
  await ctx.send("Test")
  
# RUN THE BOT:

bot.run(os.environ['token'])

# PLEASE NOTE: If you are using any public code editor, make sure the token is private. 
# Anyone can login and destroy your server through the bot.
# If you are using a public code editor, try and find some details for keeping your bot token safe on that site.
