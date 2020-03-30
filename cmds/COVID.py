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
                if nt == "0600":    #定時
                    ch = self.bot.get_channel("頻道ID")
                    await ch.send(embed = await self._GET_COVID19())    #發送
                    await asyncio.sleep(100)
                else:
                    await asyncio.sleep(10)
        self.bot.loop.create_task(infected())   #LOOP


    async def _GET_COVID19(self):   #用function回傳embed
        async with aiohttp.ClientSession() as session:
            async with session.get("https://covid19dashboard.cdc.gov.tw/dash3") as _R:
                data = (await _R.json())["0"]   #讀取資料
                emb = discord.Embed(
                    title="COVID-19疫情資訊", 
                    color=discord.Color.dark_red()
                    )
                for i in data.keys():
                    emb.add_field(name=i, value=data[i], inline=True)   #整理
                return emb


    @commands.group()
    async def COVID19(self, ctx):
        if ctx.invoked_subcommand is None:  #如果只有|COVID19
            await ctx.send(embed = await self._GET_COVID19())   #傳送


    @COVID19.command()
    async def all(self, ctx):   #|COVID19 all
        async with aiohttp.ClientSession() as session:
            async with session.get("https://covid19dashboard.cdc.gov.tw/dash2") as _R:
                data = (await _R.json())["0"]   #讀取
                items = {   #翻譯
                    "cases": "全球確定病例數",
                    "deaths": "全球死亡病例數",
                    "cfr": "全球致死率",
                    "countries": "國家/地區數"
                }
                emb = discord.Embed(
                    title="COVID-19全球疫情資訊",
                    color=discord.Color.dark_red()
                )
                for i in data.keys():
                    emb.add_field(
                        name = items[i],
                        value = data[i],
                        inline = False
                    )   #整理
                await ctx.send(embed = emb) #傳送



def setup(bot):
    bot.add_cog(COVID(bot))
