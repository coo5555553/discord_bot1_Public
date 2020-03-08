from classCog import Cog_Ext
from discord.ext import commands
import random
import discord
import json
import datetime
import pytz
import os


tz = pytz.timezone("Asia/Taipei")

with open("weeb.json", "r", encoding="utf8") as f:
    weebs = json.load(f)


class Weeb(Cog_Ext):
    @commands.command()
    async def ascii_art(self, ctx, num: int = 0):
        with open("weeb.json", "r", encoding="utf8") as f:
            weebs = json.load(f)
        if(num > weebs["ascii"]["count"]):
            await ctx.send()
        if str(ctx.author.id) in weebs["log"] and not await self.bot.is_owner(ctx.author):
            Td = weebs["log"][str(ctx.author.id)]
            delta = Td - datetime.datetime.now(tz).timestamp()
            if(delta > 0):
                await ctx.send("{0}，你還要{1}秒才能使用此指令".format(ctx.author.mention, round(delta)))
                return
        if num:
            await ctx.send(weebs["ascii"][str(num)])
        else:
            await ctx.send(weebs["ascii"][str(random.choice(range(weebs["ascii"]["count"])) + 1)])
        weebs["log"][str(ctx.author.id)] = (datetime.datetime.now(tz) + datetime.timedelta(seconds=100)).timestamp()
        with open("weeb.json", "w", encoding="utf8") as f:
            json.dump(weebs, f, indent=4, ensure_ascii=False)


    @commands.command()
    @commands.is_owner()
    async def ascii_list(self, ctx):
        with open("weeb.json", "r", encoding="utf8") as f:
            weebs = json.load(f)
        emb = discord.Embed(title="Ascii Art List", color=discord.Colour.gold(), timestamp=datetime.datetime.now(tz))
        for i in range(weebs["ascii"]["count"]):
            emb.add_field(name=f"#{i + 1}", value=weebs["ascii"][str(i + 1)], inline=False)
        await ctx.send(embed=emb)


    @commands.command()
    @commands.is_owner()
    async def ascii_add(self, ctx, *, msgs):
        with open("weebs.json", "r", encoding="utf8") as f:
            weebs = json.load(f)
        try:
            weebs["ascii"][weebs["ascii"]["count"] + 1] = ""
            for i in msgs:
                weebs["ascii"][weebs["ascii"]["count"] + 1] += i
        except Exception as e:
            await ctx.send(f"加入失敗，原因為{e}")
            return
        weebs["ascii"]["count"] += 1
        emb = discord.Embed(title="Ascii Art Added", color=discord.Colour.gold(), timestamp=datetime.datetime.now(tz))
        emb.add_field(name="#{0}".format(weebs["ascii"]["count"]), value=weebs["ascii"][weebs["ascii"]["count"]], inline=False)
        with open("weeb.json", "w", encoding="utf8") as f:
            json.dump(weebs, f, indent=4, ensure_ascii=False)
        await ctx.send(embed=emb)


    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == "AYAYA":
            with open("weeb.json", "r", encoding="utf8") as f:
                weebs = json.load(f)
            if str(msg.author.id) in weebs["log"] and not await self.bot.is_owner(msg.author):
                Td = weebs["log"][str(msg.author.id)]
                delta = Td - datetime.datetime.now(tz).timestamp()
                if(delta > 0):
                    return
            await msg.channel.send("""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣬⡛⣿⣿⣿⣯⢻ 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢻⣿⣿⢟⣻⣿⣿⣿⣿⣿⣿⣮⡻⣿⣿⣧ 
⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣆⠻⡫⣢⠿⣿⣿⣿⣿⣿⣿⣿⣷⣜⢻⣿ 
⣿⣿⡏⣿⣿⣨⣝⠿⣿⣿⣿⣿⣿⢕⠸⣛⣩⣥⣄⣩⢝⣛⡿⠿⣿⣿⣆⢝ 
⣿⣿⢡⣸⣿⣏⣿⣿⣶⣯⣙⠫⢺⣿⣷⡈⣿⣿⣿⣿⡿⠿⢿⣟⣒⣋⣙⠊ 
⣿⡏⡿⣛⣍⢿⣮⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
⣿⢱⣾⣿⣿⣿⣝⡮⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⣋⣻⣿⣿⣿⣿ 
⢿⢸⣿⣿⣿⣿⣿⣿⣷⣽⣿⣿⣿⣿⣿⣿⣿⡕⣡⣴⣶⣿⣿⣿⡟⣿⣿⣿ 
⣦⡸⣿⣿⣿⣿⣿⣿⡛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿ 
⢛⠷⡹⣿⠋⣉⣠⣤⣶⣶⣿⣿⣿⣿⣿⣿⡿⠿⢿⣿⣿⣿⣿⣿⣷⢹⣿⣿ 
⣷⡝⣿⡞⣿⣿⣿⣿⣿⣿⣿⣿⡟⠋⠁⣠⣤⣤⣦⣽⣿⣿⣿⡿⠋⠘⣿⣿ 
⣿⣿⡹⣿⡼⣿⣿⣿⣿⣿⣿⣿⣧⡰⣿⣿⣿⣿⣿⣹⡿⠟⠉⡀⠄⠄⢿⣿ 
⣿⣿⣿⣽⣿⣼⣛⠿⠿⣿⣿⣿⣿⣿⣯⣿⠿⢟⣻⡽⢚⣤⡞⠄⠄⠄⢸⣿
            """)
            weebs["log"][str(msg.author.id)] = (datetime.datetime.now(tz) + datetime.timedelta(seconds=100)).timestamp()
            with open("weeb.json", "w", encoding="utf8") as f:
                json.dump(weebs, f, indent=4, ensure_ascii=False)



    @commands.command()
    async def chika(self, ctx):
        with open("weeb.json", "r", encoding="utf8") as f:
            weebs = json.load(f)
        if str(ctx.author.id) in weebs["log"] and not await self.bot.is_owner(ctx.author):
            Td = weebs["log"][str(ctx.author.id)]
            delta = Td - datetime.datetime.now(tz).timestamp()
            if(delta > 0):
                await ctx.send("{0}，你還要{1}秒才能使用此指令".format(ctx.author.mention, round(delta)))
                return
        await ctx.send("""
⢸⣿⣿⣿⣿⠃⠄⢀⣴⡾⠃⠄⠄⠄⠄⠄⠈⠺⠟⠛⠛⠛⠛⠻⢿⣿⣿⣿⣿⣶⣤⡀⠄ 
⢸⣿⣿⣿⡟⢀⣴⣿⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣸⣿⣿⣿⣿⣿⣿⣿⣷ 
⢸⣿⣿⠟⣴⣿⡿⡟⡼⢹⣷⢲⡶⣖⣾⣶⢄⠄⠄⠄⠄⠄⢀⣼⣿⢿⣿⣿⣿⣿⣿⣿⣿ 
⢸⣿⢫⣾⣿⡟⣾⡸⢠⡿⢳⡿⠍⣼⣿⢏⣿⣷⢄⡀⠄⢠⣾⢻⣿⣸⣿⣿⣿⣿⣿⣿⣿ 
⡿⣡⣿⣿⡟⡼⡁⠁⣰⠂⡾⠉⢨⣿⠃⣿⡿⠍⣾⣟⢤⣿⢇⣿⢇⣿⣿⢿⣿⣿⣿⣿⣿ 
⣱⣿⣿⡟⡐⣰⣧⡷⣿⣴⣧⣤⣼⣯⢸⡿⠁⣰⠟⢀⣼⠏⣲⠏⢸⣿⡟⣿⣿⣿⣿⣿⣿ 
⣿⣿⡟⠁⠄⠟⣁⠄⢡⣿⣿⣿⣿⣿⣿⣦⣼⢟⢀⡼⠃⡹⠃⡀⢸⡿⢸⣿⣿⣿⣿⣿⡟ 
⣿⣿⠃⠄⢀⣾⠋⠓⢰⣿⣿⣿⣿⣿⣿⠿⣿⣿⣾⣅⢔⣕⡇⡇⡼⢁⣿⣿⣿⣿⣿⣿⢣ 
⣿⡟⠄⠄⣾⣇⠷⣢⣿⣿⣿⣿⣿⣿⣿⣭⣀⡈⠙⢿⣿⣿⡇⡧⢁⣾⣿⣿⣿⣿⣿⢏⣾ 
⣿⡇⠄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢻⠇⠄⠄⢿⣿⡇⢡⣾⣿⣿⣿⣿⣿⣏⣼⣿ 
⣿⣷⢰⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⢰⣧⣀⡄⢀⠘⡿⣰⣿⣿⣿⣿⣿⣿⠟⣼⣿⣿ 
⢹⣿⢸⣿⣿⠟⠻⢿⣿⣿⣿⣿⣿⣿⣿⣶⣭⣉⣤⣿⢈⣼⣿⣿⣿⣿⣿⣿⠏⣾⣹⣿⣿ 
⢸⠇⡜⣿⡟⠄⠄⠄⠈⠙⣿⣿⣿⣿⣿⣿⣿⣿⠟⣱⣻⣿⣿⣿⣿⣿⠟⠁⢳⠃⣿⣿⣿ 
⠄⣰⡗⠹⣿⣄⠄⠄⠄⢀⣿⣿⣿⣿⣿⣿⠟⣅⣥⣿⣿⣿⣿⠿⠋⠄⠄⣾⡌⢠⣿⡿⠃ 
⠜⠋⢠⣷⢻⣿⣿⣶⣾⣿⣿⣿⣿⠿⣛⣥⣾⣿⠿⠟⠛⠉⠄⠄
        """)
        weebs["log"][str(ctx.author.id)] = (datetime.datetime.now(tz) + datetime.timedelta(seconds=100)).timestamp()
        with open("weeb.json", "w", encoding="utf8") as f:
            json.dump(weebs, f, indent=4, ensure_ascii=False)




def setup(bot):
    bot.add_cog(Weeb(bot))