from discord.ext import commands
import os
import json
import discord


with open('settings.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
no = discord.Embed(
    title="You are not My Owner!", 
    color=discord.Color.dark_red()
)
no.set_image(url="https://i.imgur.com/Z67P5RS.gif")


bot = commands.Bot(command_prefix = '|')
bot.remove_command("help")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=jdata["GAME"]))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def load(ctx, ext):
    if await bot.is_owner(ctx.author):
        bot.load_extension(f'cmds.{ext}')
        await ctx.send(f'Loaded {ext}.')
    else:
        await ctx.send(embed=no)


@bot.command()
async def unload(ctx, ext):
    if await bot.is_owner(ctx.author):
        bot.unload_extension(f'cmds.{ext}')
        await ctx.send(f'Unloaded {ext}.')
    else:
        await ctx.send(embed=no)


@bot.command()
async def reload(ctx, ext):
    if await bot.is_owner(ctx.author):
        bot.reload_extension(f'cmds.{ext}')
        await ctx.send(f'Reloaded {ext}.')
    else:
        await ctx.send(embed=no)


for fname in os.listdir('./cmds'):
    if fname.endswith('.py'):
        bot.load_extension(f'cmds.{fname[:-3]}')


if __name__ == "__main__":
    bot.run(jdata["TOKEN"])