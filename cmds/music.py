from classCog import Cog_Ext
from discord.ext import commands
from discord.utils import get
import discord
import json
import os

with open("settings.json", "r", encoding="utf8") as jfile:
    jdata = json.load(jfile)


class Music(Cog_Ext):
    @commands.command(aliases=["j"])
    async def join(self, ctx):
        global voice
        ch = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(ch)
        else:
            voice = await ch.connect()
        await ctx.send(f"Connected to {ch}.")


    @commands.command(aliases=["l"])
    async def leave(self, ctx):
        ch = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.disconnect()
            await ctx.send(f"Disconnected from {ch}.")
        else:
            await ctx.send(f"Not in a VoiceChannel.")










def setup(bot):
    bot.add_cog(Music(bot))