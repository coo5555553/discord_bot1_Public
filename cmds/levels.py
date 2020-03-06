from classCog import Cog_Ext
from discord.ext import commands
import discord
import json
import os

os.chdir("../jsons")


class Levels(Cog_Ext):
    @commands.Cog.listener()
    async def on_message(self, msg):
        if not msg.content.isalpha():
            return
        if msg.guild.id != 611936518528958503:
            return
        with open("levels.json", "r", encoding="utf8") as jfile:
            LVL = json.load(jfile)
        ID = str(msg.author.id)
        if ID not in LVL:
            LVL[ID] = {
                "EXP": 0,
                "LV": 1
            }
            with open("levels.json", "w", encoding="utf8") as jfile:
                json.dump(LVL, jfile, indent=4)
        LVL[ID]["EXP"] += 1
        if LVL[ID]["EXP"] == LVL[ID]["LV"] * LVL[ID]["LV"]:
            LVL[ID]["LV"] += 1
            x = LVL[ID]["LV"]
            LVL[ID]["EXP"] = 0
            await msg.channel.send(f"恭喜 {msg.author.mention} 升到{x} 等！")
        with open("levels.json", "w", encoding="utf8") as jfile:
            json.dump(LVL, jfile, indent=4)


def setup(bot):
    bot.add_cog(Levels(bot))