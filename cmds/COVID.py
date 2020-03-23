from classCog import Cog_Ext
import discord
from discord.ext import commands
import datetime
import aiohttp
import asyncio
import pytz
import json


_tz = pytz.timezone("Asia/Taipei")

class COVID(Cog_Ext):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        async def infected():
            await self.bot.wait_until_ready()
            while not self.bot.is_closed():
                nt = datetime.datetime.now(_tz).strftime("%H%M")
                if nt == "0600":
                    ch = self.bot.get_channel(614709677783253002)
                    await ch.send(await self._GET_COVID19())
                    await asyncio.sleep(100)
                else:
                    await asyncio.sleep(10)
        asyncio.create_task(infected())


    async def _GET_COVID19(self):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://covid19dashboard.cdc.gov.tw/dash3") as resp:
                data = (await resp.json())["0"]
                emb = discord.Embed(
                    title="COVID-19疫情資訊", 
                    color=discord.Color.dark_red()
                    )
                for i in data.keys():
                    emb.add_field(name=i, value=data[i], inline=True)
                return emb


    @commands.command()
    async def COVID19(self, ctx):
        await ctx.send(embed = await self._GET_COVID19())


    @commands.command()
    async def test(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://covid19dashboard.cdc.gov.tw/dash3") as resp:
                data = await resp.json()
                with open("tmp.json", "w+", encoding="utf8") as _F:
                    json.dump(data, _F, indent=4, ensure_ascii=False)


def setup(bot):
    bot.add_cog(COVID(bot))