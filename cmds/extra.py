from classCog import Cog_Ext
from discord.ext import commands
import discord
import io
import os
import aiohttp
import json
import pytz
import random
import datetime
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice


os.chdir("../jsons")

tz = pytz.timezone("Asia/Taipei")

with open('settings.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class Extra(Cog_Ext):
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content.endswith("的機率") and msg.content != "的機率":
            await msg.channel.send(f'{random.randint(0, 100)}%')
            return
        if msg.content == "沒事":
            await msg.channel.send("樓上被盜")
            return
        if msg.content == "再啦" or msg.content == "在啦":
            await msg.channel.send("幹")
            return
        if msg.content == "不要瞎掰好嗎":
            async with aiohttp.ClientSession() as session:
                async with session.get("https://i.imgur.com/yTRCBCs.jpg") as resp:
                    data = io.BytesIO(await resp.read())
                    await msg.channel.send(file=discord.File(data, 'image0.png'))
                    return
        if msg.content == "並沒有":
            async with aiohttp.ClientSession() as session:
                async with session.get("https://i.imgur.com/4NkYYWw.jpg") as resp:
                    data = io.BytesIO(await resp.read())
                    await msg.channel.send(file=discord.File(data, "image0.jpg"))
                    return
        if msg.content == "怕":
            async with aiohttp.ClientSession() as session:
                async with session.get("https://i.imgur.com/yBd10LW.jpg") as resp:
                    data = io.BytesIO(await resp.read())
                    await msg.channel.send(file=discord.File(data, "image0.jpg"))

    @commands.command()
    @commands.is_owner()
    async def set_game(self, ctx, *, arg):
        jdata["GAME"] = arg
        with open("settings.json", "w", encoding="utf8") as jfile:
            json.dump(jdata, jfile, indent=4, ensure_ascii=False)
        await self.bot.change_presence(activity=discord.Game(name=jdata["GAME"]))


    @commands.command()
    @commands.has_guild_permissions(create_instant_invite=True)
    async def invite_create(self, ctx, time=100, Cnt=1):
        invit = await ctx.channel.create_invite(max_age=time, max_uses=Cnt)
        await ctx.channel.send(invit)


    @commands.command()
    async def invite_list(self,ctx):
        invites=""
        invite=await ctx.guild.invites()
        for i in invite:
            invites += f"連結：{i.url}\n"
            invites += f"創造時間：{i.created_at}\n"
            if i.max_age == 0:
                invites += f"距離過期：無限制\n"
            else:
                invites += f"距離過期：{i.max_age}\n"
            invites += f"已使用次數：{i.uses}\n"
            if i.max_uses == 0:
                invites += f"最大使用次數：無限制\n"
            else:
                invites += f"最大使用次數：{i.max_uses}\n"
            invites += f"建立人：{i.inviter.mention}\n"
            invites += ("-"*20) + "\n"
        embed1=discord.Embed(title="以下為此伺服器建立之邀請",description=invites)
        if invites == "":
            await ctx.send("此伺服器目前無邀請")
        else:
            await ctx.channel.send(embed=embed1)


    @commands.command()
    async def get_user(self, ctx, id: int = 0):
        if id:
            try:
                usr = ctx.guild.get_member(id)
                await ctx.send(f"{usr.mention}\n{usr.status}")
            except Exception as e:
                await ctx.send(f"查詢失敗，原因為{e}")
        else:
            try:
                await ctx.send(f"{ctx.author.mention}\n{ctx.guild.get_member(ctx.author.id).status}")
            except Exception as e:
                await ctx.send(f"查詢失敗，原因為{e}")


    @commands.command()
    async def fetch_user(self, ctx, id: int = 0):
        if not id:
            await ctx.channel.send("請輸入使用者ID")
            return
        else:
            try:
                usr = await self.bot.fetch_user(id)
                await ctx.channel.send(usr.mention)
            except Exception as e:
                await ctx.send(f"查詢失敗，原因為{e}")


    @commands.command()
    @commands.is_owner()
    async def rand_team(self, ctx, teams: int, count: int):
        if count < 2:
            await ctx.send("每組需要大於一人")
            return
        if teams < 1:
            await ctx.send("需要大於一組")
            return
        mems = ctx.guild.members
        onl = []
        onl_cnt = 0
        for i in mems:
            if (str(i.status) == "online" or str(i.status) == "idle") and not i.bot:
                onl.append(i)
                onl_cnt += 1
        if onl_cnt < (teams * count):
            await ctx.send("當前線上人數不足")
            return
        Embeds=[]
        for i in range(teams):
            tmpEm = discord.Embed(title=f"第{i + 1}組")
            for j in range(count):
                t = random.choice(onl)
                onl.remove(t)
                tmpEm.add_field(name=f"#{j + 1}", value=f"{t}", inline=False)
            Embeds.append(tmpEm)
        paginator = BotEmbedPaginator(ctx, Embeds)
        await paginator.run()


def setup(bot):
    bot.add_cog(Extra(bot))