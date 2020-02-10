from classCog import Cog_Ext
from discord.ext import commands
import discord
import json
import datetime
import pytz


tz = pytz.timezone("Asia/Taipei")


class Vote(Cog_Ext):
    @commands.command()
    async def vote(self, ctx, TL: str, *msgs):
        if not msgs:
            await ctx.send("請輸入投票選項")
            return
        # if " " in msg:
        #     msgs = msg.split(" ")
        # else:
        #     msgs = msg.split(",")
        if len(msgs) <= 1:
            await ctx.send("請輸入大於一個選項")
            return
        if len(msgs) > 10:
            await ctx.send("超過十個選項")
            return
        reas = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
        emb = discord.Embed(title=TL, color=discord.Color.dark_blue(), timestamp=datetime.datetime.now(tz))
        emb.set_author(name=f"發起人：{ctx.author}", icon_url=ctx.author.avatar_url)
        emb.add_field(name="以下為選項", value="============================", inline=False)
        for i in range(len(msgs)):
            emb.add_field(name=f"#{i + 1}", value=msgs[i], inline=False)
        S = await ctx.send(embed=emb)
        for i in range(len(msgs)):
            await S.add_reaction(reas[i])

        
        
        


def setup(bot):
    bot.add_cog(Vote(bot))