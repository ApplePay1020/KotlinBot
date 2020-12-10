import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("READY")
    game = discord.Game("코틀린")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("!코틀린"):
        await message.channel.send("만세!")
    if message.content.startswith("!ping"):
        await message.channel.send("pong!")
    if message.content.startswith("!SYSTEM_STATUS"):
        await message.channel.send("시러요(?)")
    if message.content.startswith("!SYSTEM_STATUS"):
        await message.channel.send("코틀린봇 상태                                                접속여부:정상")
    if message.content.startswith("!SEX"):
        await message.channel.send("ON THE BEACH")
    if message.content.startswith("!야동"):
        await message.channel.send("https://www.police.go.kr/index.do")
    if message.content.startswith("!해부"):
        await message.channel.send("97%_PYTHON , 2%_SHOTGUN , 1%_KOTLIN")
    if message.content.startswith("!여우"):
        await message.channel.send("핥쨕")
    if message.content.startswith("!SYSTEM"):
        embed = discord.Embed(title="KOTLIN[BOT] SYSTEM INFORMATION", description="KOTLIN[BOT]시스템 정보", color=0x62c1cc)
        embed.set_footer(text="version_1.0")
        await message.channel.send("", embed=embed)
    if message.content.startswith("!너 극혐"):
        await message.channel.send("......xenon?")
    if message.content.startswith("!네이버"):
        await message.channel.send("그켬")
    if message.content.startswith("!빛태현"):
        await message.channel.send("^^7")
    if message.content.startswith("!구글"):
        await message.channel.send("https://www.google.com")
    if message.content.startswith("!아잉"):
        await message.channel.send("뿌잉")
    if message.content.startswith("!코로나"):
        await message.channel.send("이겨내자!")
    if message.content.startswith("!다음"):
        await message.channel.send("https://www.daum.net/")
    if message.content.startswith("!애플"):
        await message.channel.send("채고")
    if message.content.startswith("!Apple"):
        await message.channel.send("https://www.apple.com/kr/")
    if message.content.startswith("!너"):
        await message.channel.send("숙청")
    if message.content.startswith("!img/사과"):
        pic = message.content.split(" ") [1]
        await message.channel.send(file=discord.File(pic))
    if message.content.startswith("!수능"):
        await message.channel.send("아직 멀었다")
    if message.content.startswith("!폰허브"):
        await message.channel.send("https://www.police.go.kr/index.do")

assess_token = os.environ["BOT_TOKEN"]
client.run(access_token)
