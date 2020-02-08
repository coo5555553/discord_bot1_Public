from classCog import Cog_Ext
from discord.ext import commands
import discord
import json
import pytz
import datetime
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice


tz = pytz.timezone("Asia/Taipei")
with open('settings.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class Main(Cog_Ext):
    @commands.command()
    async def help(self, ctx):
        embed1=discord.Embed(title="Main Commands", color=0xf8fe10, timestamp=datetime.datetime.now(tz))
        embed1.set_author(name="duck_test", icon_url="https://i.imgur.com/y321pla.jpg")
        embed1.add_field(name="|help", value="顯示此幫助", inline=False)
        embed1.add_field(name="|ping", value="檢測機器人的延遲", inline=False)
        embed1.add_field(name="|online_cnt", value="計算目前線上的人/機器人數", inline=False)
        embed1.set_footer(text="持續開發中...")
        embed2=discord.Embed(title="Music Commands", color=0xf8fe10, timestamp=datetime.datetime.now(tz))
        embed2.set_author(name="duck_test", icon_url="https://i.imgur.com/y321pla.jpg")
        embed2.add_field(name="|j or |join", value="加入語音頻道")
        embed2.add_field(name="|p (URL) or |play (URL)", value="播放該網址的音樂", inline=False)
        embed2.add_field(name="|l or |leave", value="離開語音頻道", inline=False)
        embed3=discord.Embed(title="Extra Commands", color=0xf8fe10, timestamp=datetime.datetime.now(tz))
        embed3.add_field(name="|invite_create (sec，預設為100，optional) (num，預設為1，optional)", value="***需要建立邀請的權限***\n建立一個壽命為sec秒，使用人數為num的邀請連結", inline=False)
        embed3.add_field(name="|invite_list", value="查看所有已建立的邀請", inline=False)
        embed3.add_field(name="|get_user (id)", value="查看使用者ID為(id)的資料", inline=False)
        embed3.add_field(name="|rand_team (組數) (人數)", value="以目前線上的使用者隨機組隊", inline=False)
        embeds = [
            embed1, embed2, embed3
        ]
        paginator = BotEmbedPaginator(ctx, embeds)
        await paginator.run()
    

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


def setup(bot):
    bot.add_cog(Main(bot))