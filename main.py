import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from random import randint

load_dotenv(".env")
TOKEN: str = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.CustomActivity(name="Gaming is epic"))
    print("Gaming Systems is now active.")

@bot.command()
async def cmds(ctx):
    embed = discord.Embed(
        color=discord.Color.dark_blue(),
        title="List of commands",
        description="!cmds - You literally sent it just now.\n\n" \
        "!mermaid - DON'T SHOW THIS TO MML OR KINEZONE!!\n\n" \
        "!generateart - see what happens\n\n" \
        "!dmoden123 - I never say Poor, ):\n\n" \
        "!nuke - ???\n\n" \
        "!nonoah - famous quotes from him.",
    )
    await ctx.send(embed=embed)

@bot.command()
async def mermaid(ctx):
    mermaidList = [
        "https://i.imgur.com/5enKzAD.png",
        "https://i.imgur.com/s25SdtE.png",
        "https://i.imgur.com/97387ea.png",
        "https://www.youtube.com/watch?v=LNgm3pebr2Y",
        "https://i.imgur.com/WiZv2ic.png",
        "https://i.imgur.com/qpXH0nt.png",
        "https://i.imgur.com/UHguIPy.jpeg",
        "https://i.imgur.com/laeRWew.png",
        "https://i.imgur.com/0gdbG7Q.png",
        "https://i.imgur.com/uubGN5A.png",
        "https://www.youtube.com/watch?v=Kte-fy6hnvw"
    ]
    await ctx.send(mermaidList[randint(0, len(mermaidList)-1)])

@bot.command()
async def generateart(ctx):
    await ctx.send("https://files.catbox.moe/ghe9r2.mp4")

@bot.command()
async def dmoden123(ctx):
    await ctx.send("Roblox im sorry... I never Say poor, ): im so sorry roblox do not ban me, then im so sad cuz pls roblox read this, somthing is inside of me... like a ghost? pls help me roblox, Im getting hacked.-- pls help me. your Dmoden123.")

@bot.command()
async def nuke(ctx):
    await ctx.send("https://i.imgur.com/WGqhPM5.png")

@bot.command()
async def nonoah(ctx):
    await ctx.send("as nonoah0001 once said:")
    list = [
        "gaming is epic",
        "yes",
        "NO MERMAID ALLOWED GRRRRRRRRRR",
        "WHAT",
        "O",
        "Fun is allowed"
    ]
    await ctx.send(list[randint(0, len(list)-1)])

bot.run(os.getenv("TOKEN"))