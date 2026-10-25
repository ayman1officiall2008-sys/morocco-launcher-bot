
import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Morocco Launcher is online as {bot.user}")

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="welcome")
    if channel:
        await channel.send(
            f"🇲🇦 مرحبا {member.mention} فـ **Morocco Launcher**! نورت السيرفر."
        )

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong! البوت خدام.")

@bot.command()
async def helpme(ctx):
    await ctx.send(
        "**Morocco Launcher Commands**\n"
        "`!ping` - اختبار البوت\n"
        "`!mc` - معلومات سيرفر Minecraft خاصها إعداد إضافي"
    )

@bot.command()
async def mc(ctx):
    await ctx.send("⛏️ غادي نربطو حالة Minecraft فخطوة جاية!")

bot.run(TOKEN)
