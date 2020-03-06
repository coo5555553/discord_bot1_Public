from discord.ext import commands
from classCog import Cog_Ext
import discord
import os
import json
import requests
import asyncio

os.chdir("../jsons")

with open("alert.json", "r", encoding="utf8") as f:
    URL = json.load(f)["URL"]


def gen_emb(data):
    emb = discord.Embed(title="地震資訊#{0}".format(data["earthquakeNo"]), 
                        color=discord.Color.dark_red())
    emb.set_image(url=data["reportImageURI"])
    emb.add_field(name="發生時間", value=data["earthquakeInfo"]["originTime"], inline=False)
    emb.add_field(name="震央位置", value=data["earthquakeInfo"]["epiCenter"]["location"], inline=False)
    emb.add_field(name="震源深度", value="{0}公里".format(data["earthquakeInfo"]["depth"]["value"]), inline=False)
    emb.add_field(name="芮氏規模", value=data["earthquakeInfo"]["magnitude"]["magnitudeValue"])
    area = ""
    for i in data["intensity"]["shakingArea"]:
        if "最大震度" in i["areaDesc"]:
            if i["areaIntensity"]["value"] >= 3:
                area += "{0} {1}級\n".format(i["areaName"], i["areaIntensity"]["value"])
            elif i["areaIntensity"]["value"] == 2 and "臺北市" in i["areaName"]:
                if "新北市" in i["areaName"]:
                    area += "臺北市、新北市 2級\n"
                else:
                    area += "臺北市 2級\n"
            elif i["areaIntensity"]["value"] == 2 and "新北市" in i["areaName"]:
                area += "新北市 2級\n"
    if area == "":
        emb.add_field(name="各地最高震度(只列出3級以上)", value="無", inline=False)
    else:
        emb.add_field(name="各地最高震度(只列出3級以上)", value=area, inline=False)
    return emb


class Alert(Cog_Ext):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        async def rep():
            await self.bot.wait_until_ready()
            while not self.bot.is_closed():
                data = requests.get(URL).json()["records"]["earthquake"][0]
                with open("alert.json", "r", encoding="utf8") as f:
                    jdata = json.load(f)
                if data["earthquakeNo"] > jdata["No"]:
                    jdata["No"] = data["earthquakeNo"]
                    with open("alert.json", "w", encoding="utf8") as f:
                        json.dump(jdata, f, indent=4, ensure_ascii=False)
                    await self.bot.get_channel(jdata["CHANNEL"]).send(embed=gen_emb(data))
                else:
                    await asyncio.sleep(5)
        self.bot.loop.create_task(rep())


    @commands.command()
    async def latest_EQ(self, ctx):
        data = requests.get(URL).json()["records"]["earthquake"][0]
        await ctx.send(embed=gen_emb(data))


    @commands.command()
    async def alert_ch(self, ctx, cid: int):
        with open("alert.json", "r", encoding="utf8") as f:
            tmp = json.load(f)
            tmp["CHANNEL"] = cid
        with open("alert.json", "w", encoding="utf8") as f:
            json.dump(tmp, f, ensure_ascii=False, indent=4)
        await ctx.send("Alert channel set to {0}".format(self.bot.get_channel(cid).mention))
        


def setup(bot):
    bot.add_cog(Alert(bot))