from classCog import Cog_Ext
from discord.ext import commands
import discord
import io
import aiohttp
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
        if msg.content == "再啦" or msg.content == "在啦":
            await msg.channel.send("幹")
        if msg.content == "不要瞎掰好嗎":
            async with aiohttp.ClientSession() as session:
                async with session.get("https://i.imgur.com/yTRCBCs.jpg") as resp:
                    data = io.BytesIO(await resp.read())
                    await msg.channel.send(file=discord.File(data, 'dontxiabye.png'))
        if msg.content == "並沒有":
            async with aiohttp.ClientSession() as session:
                async with session.get("https://i.imgur.com/4NkYYWw.jpg") as resp:
                    data = io.BytesIO(await resp.read())
                    await msg.channel.send(file=discord.File(data, "bingmeiyou.jpg"))


    @commands.command()
    async def setgame(self, ctx, *, arg):
        if ctx.author.id == jdata["DUCK_ID"]:
            jdata["GAME"] = arg
            with open("settings.json", "w", encoding="utf8") as jfile:
                json.dump(jdata, jfile, indent=4)
            await self.bot.change_presence(activity=discord.Game(name=jdata["GAME"]))


    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency * 1000)} (ms)')


def setup(bot):
    bot.add_cog(Extra(bot))