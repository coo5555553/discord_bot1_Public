from classCog import Cog_Ext
from discord.ext import commands
import discord
import random


class Gamble(Cog_Ext):
    @commands.command()
    async def roll(self, ctx, cnt: int=1):
        if cnt < 1:
            await ctx.send("請輸入大於等於一的正整數")
            return
        msg = "您骰出了"
        nums = random.choices(range(1, 7), k = cnt)
        for i in range(cnt):
            msg += str(nums[i])
            if i != cnt - 1:
                msg += ", "
        await ctx.send(msg)



def setup(bot):
    bot.add_cog(Gamble(bot))