from classCog import Cog_Ext
from discord.ext import commands
import discord
import os
import json
import pytz
import datetime

tz = pytz.timezone("Asia/Taipei")


class Main(Cog_Ext):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency * 1000)} (ms)')


    @commands.command()
    async def online_cnt(self, ctx):
        mems = ctx.guild.members
        onl_cnt = 0
        onl_bot = 0
        for i in mems:
            if str(i.status) == "online":
                if i.bot:
                    onl_bot += 1
                else:
                    onl_cnt += 1
        await ctx.send(f"當前線上為{onl_cnt}人和{onl_bot}個機器人")


    @commands.command()
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, id: discord.User, *, reas=None):
        try:
            await ctx.guild.kick(id)
        except Exception as e:
            await ctx.send(f"踢出使用者失敗，原因為{e}\n")
            return
        else:
            await ctx.send(f"`已踢出 **{id.mention}**\n原因為 {reas}`")


    @commands.command(aliases = ["vm"])
    @commands.is_owner()
    async def voice_move(self, ctx, ch1: int, ch2: int):
        A = self.bot.get_channel(ch1)
        B = self.bot.get_channel(ch2)
        for i in A.members:
            await i.move_to(B)


    @commands.command()
    @commands.is_owner()
    async def avatar(self, ctx, usr: discord.User):
        await ctx.send(usr.avatar_url)



def setup(bot):
    bot.add_cog(Main(bot))
