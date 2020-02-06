from discord.ext import commands
import os
import json
import discord


with open('settings.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


bot = commands.Bot(command_prefix = '|')
bot.remove_command("help")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="test"))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def load(ctx, ext):
    if ctx.author.id == jdata["DUCK_ID"]:
        bot.load_extension(f'cmds.{ext}')
        await ctx.send(f'Loaded {ext}.')
    else:
        await ctx.send("You Don't Have the Permission to Use this Command!")


@bot.command()
async def unload(ctx, ext):
    if ctx.author.id == jdata["DUCK_ID"]:
        bot.unload_extension(f'cmds.{ext}')
        await ctx.send(f'Unloaded {ext}.')
    else:
        await ctx.send("You Don't Have the Permission to Use this Command!")


@bot.command()
async def reload(ctx, ext):
    if ctx.author.id == jdata["DUCK_ID"]:
        bot.reload_extension(f'cmds.{ext}')
        await ctx.send(f'Reloaded {ext}.')
    else:
        await ctx.send("You Don't Have the Permission to Use this Command!")


for fname in os.listdir('./cmds'):
    if fname.endswith('.py'):
        bot.load_extension(f'cmds.{fname[:-3]}')


if __name__ == "__main__":
    bot.run(jdata["TOKEN"])