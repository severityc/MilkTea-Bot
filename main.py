import discord
import json
import asyncio
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Bot is online!')

@bot.command()
async def backup(ctx):
    if ctx.channel.type != discord.ChannelType.text:
        return await ctx.send('This command can only be used in a server text channel.')

    try:
        with open('data/backup.txt', 'r') as file:
            description = file.read().strip()
    except FileNotFoundError:
        return await ctx.send('Description file not found.')

    embed = discord.Embed(title='Backup Information', description=description)

    await ctx.send(embed=embed)

@bot.command()
async def rules(ctx):
    if ctx.channel.type != discord.ChannelType.text:
        return await ctx.send('This command can only be used in a server text channel.')

    try:
        with open('data/rules.txt', 'r') as file:
            description = file.read().strip()
    except FileNotFoundError:
        return await ctx.send('Description file not found.')

    embed = discord.Embed(title='SERVER RULES', description=description)

    await ctx.send(embed=embed)

@bot.command()
async def verify(ctx):
    if ctx.channel.type != discord.ChannelType.text:
        return await ctx.send('This command can only be used in a server text channel.')

    try:
        with open('data/verify.txt', 'r') as file:
            description = file.read().strip()
    except FileNotFoundError:
        return await ctx.send('Description file not found.')

    embed = discord.Embed(title='Verification', description=description)
    
    button = discord.ui.Button(label="Verify", url="https://discord.com/oauth2/authorize?client_id=1221190700805128322&redirect_uri=https://milktea.novanode.win/&response_type=code&scope=identify+guilds.join&state=no-captcha")
    
    view = discord.ui.View()
    view.add_item(button)

    await ctx.send(embed=embed, view=view)

@bot.command()
async def invite_rewards(ctx):
    if ctx.channel.type != discord.ChannelType.text:
        return await ctx.send('This command can only be used in a server text channel.')

    try:
        with open('data/invite_rewards.txt', 'r') as file:
            description = file.read().strip()
    except FileNotFoundError:
        return await ctx.send('Description file not found.')

    embed = discord.Embed(title='🎁 Invite Rewards', description=description)
    
    button = discord.ui.Button(label="Claim Reward", url="https://discord.com/channels/1204976590161846302/1205008246348451850/1215450295660978227")
    
    view = discord.ui.View()
    view.add_item(button)

    await ctx.send(embed=embed, view=view)

@bot.command()
async def boost_rewards(ctx):
    if ctx.channel.type != discord.ChannelType.text:
        return await ctx.send('This command can only be used in a server text channel.')

    try:
        with open('data/boost_rewards.txt', 'r') as file:
            description = file.read().strip()
    except FileNotFoundError:
        return await ctx.send('Description file not found.')

    embed = discord.Embed(title='🚀 Boost Rewards', description=description)
    
    button = discord.ui.Button(label="Claim Reward", url="https://discord.com/channels/1204976590161846302/1205008246348451850/1215450295660978227")
    
    view = discord.ui.View()
    view.add_item(button)

    await ctx.send(embed=embed, view=view)

    #############################

@bot.command()
async def drop(ctx):
    await ctx.send("How do you want to send the file? Type 'normal' for normal text or 'txt' for a text file.")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() in ['normal', 'txt']

    try:
        response = await bot.wait_for('message', check=check, timeout=30)
        file_path = 'drop/sigma.txt'

        if response.content.lower() == 'normal':
            with open(file_path, 'r', encoding='utf-8') as file:
                contents = file.read()
            await ctx.send(contents)
        elif response.content.lower() == 'txt':
            with open(file_path, 'rb') as file:
                file_contents = discord.File(file)
                await ctx.send(file=file_contents)

    except asyncio.TimeoutError:
        await ctx.send("You took too long to respond.")
    except FileNotFoundError:
        await ctx.send("The specified file does not exist.")

    
# Bot Token via config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    token = config.get('token')

bot.run(token)