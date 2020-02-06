from classCog import Cog_Ext
from discord.ext import commands
import os
import time
import pytz
import json
import discord
import asyncio
import datetime


tz = pytz.timezone("Asia/Taipei")


class Countdown(Cog_Ext):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cnt = 0

        # async def interval():
        #     await self.bot.wait_until_ready()
        #     self.channel = self.bot.get_channel(611936518528958508)
        #     while not self.bot.is_closed():
        #         await self.channel.send("test")
        #         await asyncio.sleep(10)


        # self.bg_task1 = self.bot.loop.create_task(interval())

        async def cd():
            await self.bot.wait_until_ready()
            with open("settings.json", "r", encoding="utf8") as jfile:
                jdata = json.load(jfile)
            self.channel = self.bot.get_channel(jdata["CHANNEL"])
            d1 = datetime.date(2020, 2, 24)
            d2 = datetime.date(2020, 7, 1)
            d3 = datetime.date(2020, 5, 16)
            d4 = datetime.date(2020, 5, 2)
            while not self.bot.is_closed():
                nt = datetime.datetime.now(tz).strftime('%H%M')
                with open("settings.json", "r", encoding="utf8") as jfile:
                    jdata = json.load(jfile)
                if nt == jdata["TIME"] and self.cnt == 0:
                    self.cnt = 1
                    time_2day = datetime.datetime.now(tz)
                    await self.channel.send('@everyone' + """css
[放榜   (02/24)]還有( """ + str((d1 - time_2day).days - 1) + """ Day )
[TVE   (05/02)]還有( """ + str((d4 - time_2day).days - 1) + """ Day )
[CAP   (05/16)]還有( """ + str((d3 - time_2day).days - 1) + """ Day )
[AST   (07/01)]還有( """ + str((d2 - time_2day).days - 1) + """ Day )
""")
                    await asyncio.sleep(60)
                else:
                    self.cnt = 0
                    await asyncio.sleep(1)
        self.bg_task = self.bot.loop.create_task(cd())


    @commands.command()
    async def set_channel(self, ctx, ch: int):
        with open("settings.json", "r", encoding="utf8") as jfile:
            jdata = json.load(jfile)
        self.channel = self.bot.get_channel(ch)
        jdata["CHANNEL"] = ch
        with open("settings.json", "w", encoding="utf8") as jfile:
            json.dump(jdata, jfile, indent=4)
        await ctx.send(f'Set Channel to {self.channel.mention}')

    
    @commands.command()
    async def set_time(self, ctx, time):
        with open("settings.json", "r", encoding="utf8") as jfile:
            jdata = json.load(jfile)
        self.cnt = 0
        jdata["TIME"] = time
        with open("settings.json", "w", encoding="utf8") as jfile:
            json.dump(jdata, jfile, indent=4)
        await ctx.send(f'Set Time to {time}')


    @commands.command()
    async def time(self, ctx):
        await ctx.send(datetime.datetime.now(tz))


    @commands.command()
    async def test(self, ctx):
        d1 = datetime.date(2020, 2, 24)
        d2 = datetime.date(2020, 7, 1)
        d3 = datetime.date(2020, 5, 16)
        d4 = datetime.date(2020, 5, 2)
        time_2day = datetime.datetime.now(tz).date()
        await ctx.send('@everyone' + """```css
[放榜   (02/24)]還有( """ + str((d1 - time_2day).days) + """ Day )
[TVE   (05/02)]還有( """ + str((d4 - time_2day).days) + """ Day )
[CAP   (05/16)]還有( """ + str((d3 - time_2day).days) + """ Day )
[AST   (07/01)]還有( """ + str((d2 - time_2day).days) + """ Day )
```""")


def setup(bot):
    bot.add_cog(Countdown(bot))