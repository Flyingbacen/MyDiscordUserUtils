# necessary imports
""""""
import discord
import asyncio
""""""
import json
""""""
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)
""""""
@tree.command()
async def ping(ctx):
    await ctx.send("Pong!")
    # test

@client.event
async def on_ready():
	await tree.sync()
	print("Ready!")

client.run(json.load(open("config.json"))["token"])