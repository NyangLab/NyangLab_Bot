import discord, os, random

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command(description="말 그대로 도움말")
async def help(ctx):
    embed = discord.Embed(title="도움말", color=0x3a88fe)
    embed.add_field(name="이제 복잡한 help 명령어는 안녕~", value="이제는 슬커만 입력해도 충분한 세상이 왔어요!", inline=True)
    await ctx.respond(embed=embed)

@bot.slash_command(description="가위바위보? 아니 니 주먹냈잖아 왜 가위로 바꿔! (가위, 바위, 보 로만 입력받습니다.)")
async def 가위바위보(ctx, user: str):  # user:str로 !game 다음에 나오는 메시지를 받아줌
    rps_table = ['가위', '바위', '보']
    bot_choice = random.choice(rps_table)
    result = rps_table.index(user) - rps_table.index(bot_choice)  # 인덱스 비교로 결과 결정
    if result == 0:
        embed = discord.Embed(title="비겼습니다.")
        embed.add_field(name=ctx.author.display_name, value=user, inline=True)
        embed.add_field(name="👑 Bot", value=bot_choice, inline=True)
        embed.set_footer(text=f"{ctx.author.display_name} vs 👑 Bot", icon_url="")
        await ctx.respond(embed=embed)
    elif result == 1 or result == -2:
        embed = discord.Embed(title="유저가 이겼습니다.")
        embed.add_field(name=f"👑 {ctx.author.display_name}", value=user, inline=True)
        embed.add_field(name="Bot", value=bot_choice, inline=True)
        embed.set_footer(text=f"👑 {ctx.author.display_name} vs Bot", icon_url="")
        await ctx.respond(embed=embed)
    else:
        embed = discord.Embed(title="봇이 이겼습니다.")
        embed.add_field(name=ctx.author.display_name, value=user, inline=True)
        embed.add_field(name="👑 Bot", value=bot_choice, inline=True)
        embed.set_footer(text=f"{ctx.author.display_name} vs Bot", icon_url="")
        await ctx.respond(embed=embed)

@bot.slash_command(description="우리 html 오류 코드를 재미있는 고양이로 알아볼까요? (오류 코드만 입력)")
async def httpcat(ctx, httperror:str):
    if httperror >= "600":
        embed=discord.Embed(title="real 404")
        embed.set_author(name="http.cat", url="https://http.cat")
        embed.set_image(url=f"https://http.cat/404")
        await ctx.respond(embed=embed)
    else:
        embed=discord.Embed(title="meow")
        embed.set_author(name="http.cat", url="https://http.cat")
        embed.set_image(url=f"https://http.cat/{httperror}")
        await ctx.respond(embed=embed)

bot.run(os.getenv('NYANGLAB_DPY_TOKEN'))
