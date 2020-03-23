from discord.ext import commands
from classCog import Cog_Ext
import discord
import asyncio
import json
import aiohttp
import pytz
import os
import datetime


tz = pytz.timezone("Asia/Taipei")

with open("weather.json", "r", encoding="utf8") as f:
    URL = json.load(f)["URL"]


async def area_gen_emb(area, county):

    with open("area.json", "r", encoding = "utf8") as f:
        CT = json.load(f)[area]
    async with aiohttp.ClientSession() as session:
        async with session.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/\
            F-D0047-{0}?\
                Authorization=CWB-D405E9F2-0F0E-449E-B0CC-98E4AC01AA1B&\
                    limit=1".format(CT)) as rep:
            pass



async def gen_emb(area):
    area = area.replace("台", "臺")
    async with aiohttp.ClientSession() as session:
        async with session.get(URL + area) as _R:
            data = (await _R.json())["records"]["location"][0]["weatherElement"]
            items = {}
            types = {
                "Wx": ["天氣狀況", ""],
                "PoP": ["降雨率", "%"],
                "MinT": ["最低溫", "°C"],
                "MaxT": ["最高溫", "°C"],
                "CI": ["舒適度", ""]
            }
            for i in data[0]["time"]:
                items[i["startTime"]] = {
                    "value": "",
                    "endTime": i["endTime"]
                }
            emb = discord.Embed(
                title="{0}地區今明36小時天氣預報".format(area)
                )
            for item in data:
                for t in item["time"]:
                    items[t["startTime"]]["value"] += "{0}：{2} {1}\n"\
                        .format(
                            types[item["elementName"]][0], 
                            types[item["elementName"]][1], 
                            t["parameter"]["parameterName"]
                            )
            for K in items.keys():
                emb.add_field(name="{0} ~ {1}".format(
                    K, 
                    items[K]["endTime"]
                    ), value=items[K]["value"], inline=False)
            return emb


async def Ex_gen_emb():
    emb = discord.Embed(title="各直轄市十二小時內天氣概況", discription="#")
    contries = ["臺北市", "新北市", "桃園市", "臺中市", "臺南市", "高雄市"]
    types = {
        "Wx": ["天氣狀況", ""],
        "PoP": ["降雨率", "%"],
        "MinT": ["最低溫", "°C"],
        "MaxT": ["最高溫", "°C"]
    }
    for i in contries:
        tmp = ""
        async with aiohttp.ClientSession() as session:
            async with session.get(URL + i) as _R:
                data = (await _R.json())["records"]["location"][0]["weatherElement"]
                for item in data:
                    if item["elementName"] in ["Wx", "PoP", "MaxT", "MinT"]:
                        tmp += "{0}：{2} {1}\n"\
                            .format(
                                types[item["elementName"]][0],
                                types[item["elementName"]][1],
                                item["time"][0]["parameter"]["parameterName"]
                                )
                emb.add_field(name=i, value=tmp, inline=False)
    return emb


class Weather(Cog_Ext):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        async def timeWeather():
            await self.bot.wait_until_ready()
            while not self.bot.is_closed():
                nt = datetime.datetime.now(tz).strftime("%H%M")
                if nt == "0600" or nt == "1800":
                    ch = self.bot.get_channel(682070501233000467)
                    await ch.purge()
                    await ch.send(embed = await Ex_gen_emb())
                    await asyncio.sleep(60)
                else:
                    await asyncio.sleep(1)
        self.bot.loop.create_task(timeWeather())
            

    @commands.command()
    async def weather(self, ctx, *, arg):
        await ctx.send(embed = await gen_emb(arg))


    @commands.command()
    async def now_weather(self, ctx, *, arg):
        async with aiohttp.ClientSession() as session:
            async with session.get(URL + arg) as _R:
                data = (await _R.json())["records"]["location"][0]["weatherElement"]
                items = ""
                types = {
                    "Wx": ["天氣狀況", ""],
                    "PoP": ["降雨率", "%"],
                    "MinT": ["最低溫", "°C"],
                    "MaxT": ["最高溫", "°C"],
                    "CI": ["舒適度", ""]
                }
                emb = discord.Embed(
                    title="{0}地區即時天氣資訊".format(arg), 
                    discription="#"
                    )
                for item in data:
                    items += "{0}：{2} {1}\n"\
                        .format(
                            types[item["elementName"]][0], 
                            types[item["elementName"]][1], 
                            item["time"][0]["parameter"]["parameterName"]
                            )
                emb.add_field(
                    name="~ {0}".format(data[0]["time"][0]["endTime"]), 
                    value=items, inline=False)
                await ctx.send(embed=emb)


    @commands.command()
    async def area_weather(self, ctx, city, county):
        city = city.replace("台", "臺")
        

def setup(bot):
    bot.add_cog(Weather(bot))