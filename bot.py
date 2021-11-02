# temp place to work on a basic bot
import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print("We are Ready to roll as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return # do nothing to my own messages
  
  if message.content.startswith('$ping'):
    await message.channel.send("Pong!")
client.run(os.getenv('TOKEN'))
