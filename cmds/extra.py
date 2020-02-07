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


    @commands.command()
    async def invite_create(self, ctx, time=100):
        invit = await ctx.channel.create_invite(max_age=time)
        await ctx.channel.send(invit)


    @commands.command()
    async def invite_list(self,ctx):
        channels=ctx.guild.channels
        invites=""
        invite=await ctx.guild.invites()
        for i in invite:
            invites += f"連結：{i.url}\n"
            invites += f"創造時間：{i.created_at}\n"
            if i.max_age == 0:
                invites += f"距離過期：無限制"
            else:
                invites += f"距離過期：{i.max_age}"
            invites += f"已使用次數：{i.uses}\n"
            if i.max_uses == 0:
                invites += f"最大使用次數：無限制\n"
            else:
                invites += f"最大使用次數：{i.max_uses}\n"
            invites += f"建立於頻道：<#{i.channel.id}>\n"
            invites += f"建立人：{i.inviter.mention}\n"
            invites += ("-"*20) + "\n"
        embed1=discord.Embed(title="以下為此伺服器建立之邀請",description=invites)
        await ctx.channel.send(embed=embed1)


def setup(bot):
    bot.add_cog(Extra(bot))