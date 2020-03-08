from discord.ext import commands
import os
import json
import discord
import sys
import traceback
import asyncio


os.chdir("./jsons")
bot = commands.Bot(command_prefix = '|')
bot.remove_command("help")


@bot.event
async def on_ready():
    with open('settings.json', 'r', encoding='utf8') as jfile:
        jdata = json.load(jfile)
    await bot.change_presence(activity=discord.Game(name=jdata["GAME"]))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
@commands.is_owner()
async def load(ctx, ext):
    bot.load_extension(f'cmds.{ext}')
    await ctx.send(f'Loaded {ext}.')


@bot.command()
@commands.is_owner()
async def unload(ctx, ext):
    bot.unload_extension(f'cmds.{ext}')
    await ctx.send(f'Unloaded {ext}.')


@bot.command()
@commands.is_owner()
async def reload(ctx, ext):
    bot.reload_extension(f'cmds.{ext}')
    await ctx.send(f'Reloaded {ext}.')


for fname in os.listdir('../cmds'):
    if fname.endswith('.py'):
        bot.load_extension(f'cmds.{fname[:-3]}')


if __name__ == "__main__":
    with open('settings.json', 'r', encoding='utf8') as jfile:
        jdata = json.load(jfile)
    bot.run(jdata["TOKEN"])