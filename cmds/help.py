from discord.ext import commands
from classCog import Cog_Ext
import discord
from disputils import BotEmbedPaginator

class Help(Cog_Ext):
    @commands.group()
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            msg = discord.Embed(
                title = "All Commands", 
                description = "Use `|help <catagory>` for more help",
                color = discord.Color.green()
                )
            msg.add_field(
                name = "Main．4", 
                value = "`|kick`, `|online_cnt`, `|ping`, `|voice_move`", 
                inline = False
                )
            msg.add_field(
                name = "Alert．1", 
                value = "`|latest_EQ`", 
                inline = False
            )
            msg.add_field(
                name = "Extra．4", 
                value = "`|fetch_user`, `|get_user`, `|invite_create`, `|invite_list`", 
                inline = False
            )
            msg.add_field(
                name = "Gamble．1", 
                value = "`|roll`", 
                inline = False
            )
            msg.add_field(
                name = "Vote．1", 
                value = "`|vote`", 
                inline = False
            )
            msg.add_field(
                name = "Weather．2", 
                value = "`|weather`, `|weather_now`", 
                inline = False
            )
            await ctx.send(embed=msg)


    @help.command()
    async def main(self, ctx):
        msg = """```md
< Main Commands List >
|kick <使用者>
#踢出指定成員
|online_cnt
#計算線上人數
|ping
#檢測機器人延遲
|voice_move <語音頻道1> <語音頻道2>
|vm <語音頻道1> <語音頻道2>
#把語音頻道1的使用者移動到語音頻道2
```"""
        await ctx.send(msg)


    @help.command()
    async def alert(self, ctx):
        msg = """```md
< Alert Commands List >
|latest_EQ
#查詢最近一次的地震資訊
```"""
        await ctx.send(msg)


    @help.command()
    async def extra(self, ctx):
        msg = """```md
< Extra Commands List >
|get_user <用戶>
#查詢該使用者及其線上狀態 (機器人必須與其有共同伺服器)
|fetch_user <用戶>
#獲得該使用者的資訊 (機器人不必與其有共同伺服器)
|invite_create <T> <C>
#創建一個耐久為T秒(預設100秒)，C次(預設1次)的伺服器邀請
|invite_list
#查看伺服器的邀請列表
```"""
        await ctx.send(msg)


    @help.command()
    async def gamble(self, ctx):
        msg = """```md
< Gamble Commands List >
|roll <C>
#擲C枚骰子(預設1枚)
```"""
        await ctx.send(msg)


    @help.command()
    async def vote(self, ctx):
        msg = """```md
< Vote Commands List >
|vote <標題> <選項>
#建立投票
```"""
        await ctx.send(msg)
    

    @help.command()
    async def weather(self, ctx):
        msg = """
        ```md
< Weather Commands List >
|weather <縣市>
#查詢該縣市24(或36)小時內的氣候概況
|weather_now <縣市>
#查詢該縣市目前的天氣概況
```"""
        await ctx.send(msg)


def setup(bot):
    bot.add_cog(Help(bot))