from discord_bot1.classCog import Cog_Ext
from discord.ext import commands
import discord
import json
import pytz
import random
import datetime


tz = pytz.timezone("Asia/Taipei")
with open('settings.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class Extra(Cog_Ext):
    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title="Help", description="指令表", color=0xedf72d, timestamp=datetime.datetime.now(tz))
        embed.set_author(name="duck_test", icon_url="https://i.imgur.com/y321pla.jpg")
        embed.set_thumbnail(url="https://i.imgur.com/zPRb1e9.png")
        embed.add_field(name="--------基本功能--------", value="|help 顯示此視窗\n|ping 測試機器人的延遲", inline=True)
        embed.set_footer(text="持續開發中...\n")
        await ctx.send(embed=embed)


    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content.endswith("的機率") and msg.content != "的機率":
            await msg.channel.send(f'{random.randint(0, 100)}%')
        if msg.content == "沒事":
            await msg.channel.send("樓上被盜")
        if msg.content == "怕":
            await msg.channel.send("怕三小，沒被壓路機砸過484")
        if msg.content == "並沒有":
            img = discord.File("images\\dontshabai.jpg")
            await msg.channel.send(file=img)


    @commands.command()
    async def setgame(self, ctx, msg):
        if ctx.author.id == jdata["DUCK_ID"]:
            await self.bot.change_presence(activity=discord.Game(name=msg))


    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency * 1000)} (ms)')

        
def setup(bot):
    bot.add_cog(Extra(bot))