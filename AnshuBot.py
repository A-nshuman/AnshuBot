import discord
from discord.ext import commands
from random import choice
import math
from math import *
import random
import wikipedia
import asyncio
from discord import Member
import pyjokes
import aiohttp

intents = discord.Intents.default()

intents.members = True

client = commands.Bot(command_prefix = '.', intents=intents)
client.sniped_message = {}

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('with MrAnshuman#1060'))
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

@client.event
async def on_message_delete(message):
    client.sniped_message[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)

@client.command()
async def snipe(ctx):
    try:
        contents, author, channel_name, time =  client.sniped_message[ctx.guild.id]

    except:
        await ctx.channel.send("Couldn't find a message to snipe")
        return

    embed = discord.Embed(description = contents, colour = discord.Colour.random(), timestmp = time)
    embed.set_author(name = f"{author.name}#{author.discriminator}", icon_url = author.avatar_url)
    embed.set_footer(text = f"Deleted in : #{channel_name}")

    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send(f'**Pong!** {round(client.latency * 1000)}ms')

@client.command(aliases=['del'])
async def delete(ctx, amount=1):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick_server(ctx, member : discord.Member):
    await member.kick()
    await ctx.send(f'Kicked {member.mention}')

@client.command()
async def ban(ctx, member : discord.Member):
    await member.ban()
    await ctx.send(f'Banned {member.mention}')

@client.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)

@client.command()
async def unban(ctx, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (user_name, user_discriminator):
            await ctx.guild.unbn(user)
            await ctx.send(f'unbanned {user.name}#{user.discriminator}')

@client.command()
async def toss(ctx):

    coin = ['Head',
            'Tail']

    embed = discord.Embed(title = "Toss", description = f"{random.choice(coin)}", colour = discord.Colour.blue(), timestamp = ctx.message.created_at)
    embed.set_footer(text="Anshuman's Bot")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/827952858732298302/828706324212088832/toss_1.png')
    embed.add_field(name = "Coin Tossed by", value = f"{ctx.author.mention}")
    await ctx.send(embed=embed)

@client.command()
async def roll(ctx):
    embed = discord.Embed(title = "Die Rolled", description = (random.randint(1, 7)), color = (0xF85252), timestamp=ctx.message.created_at)
    embed.set_footer(text=f"Anshuman's Bot")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/827952858732298302/828707070852202576/dice_2_edt.png')
    embed.add_field(name = "Die Rolled by", value = f"{ctx.author.mention}")
    await ctx.send(embed = embed)

@client.command()
async def loadout(ctx):
    weapon = ['https://static.wikia.nocookie.net/valorant/images/b/b6/Stinger.png/revision/latest/scale-to-width-down/200?cb=20200404170849',
            'https://static.wikia.nocookie.net/valorant/images/9/90/Spectre.png/revision/latest/scale-to-width-down/200?cb=20200404170922',
            'https://static.wikia.nocookie.net/valorant/images/e/eb/Bucky.png/revision/latest/scale-to-width-down/200?cb=20200404171832',
            'https://static.wikia.nocookie.net/valorant/images/8/8a/Judge.png/revision/latest/scale-to-width-down/200?cb=20200404171858',
            'https://static.wikia.nocookie.net/valorant/images/0/07/Bulldog.png/revision/latest/scale-to-width-down/200?cb=20200404171103',
            'https://static.wikia.nocookie.net/valorant/images/f/fd/Guardian.png/revision/latest/scale-to-width-down/200?cb=20200404171224',
            'https://static.wikia.nocookie.net/valorant/images/e/ec/Phantom.png/revision/latest/scale-to-width-down/200?cb=20200404171302',
            'https://static.wikia.nocookie.net/valorant/images/5/56/Vandal.png/revision/latest/scale-to-width-down/200?cb=20200404171348',
            'https://static.wikia.nocookie.net/valorant/images/b/b9/Marshal.png/revision/latest/scale-to-width-down/200?cb=20200404172126',
            'https://static.wikia.nocookie.net/valorant/images/1/17/Operator.png/revision/latest/scale-to-width-down/200?cb=20200404172152',
            'https://static.wikia.nocookie.net/valorant/images/0/05/Ares.png/revision/latest/scale-to-width-down/200?cb=20200404171957',
            'https://static.wikia.nocookie.net/valorant/images/5/58/Odin.png/revision/latest/scale-to-width-down/200?cb=20200404172022']

    pistol = ['https://static.wikia.nocookie.net/valorant/images/5/57/Classic.png/revision/latest/scale-to-width-down/130?cb=20200404154125',
            'https://static.wikia.nocookie.net/valorant/images/7/77/Shorty.png/revision/latest/scale-to-width-down/170?cb=20200404154222',
            'https://static.wikia.nocookie.net/valorant/images/f/f1/Frenzy.png/revision/latest/scale-to-width-down/130?cb=20200404154617',
            'https://static.wikia.nocookie.net/valorant/images/a/ab/Ghost.png/revision/latest/scale-to-width-down/170?cb=20200404154731',
            'https://static.wikia.nocookie.net/valorant/images/3/3e/Sheriff.png/revision/latest/scale-to-width-down/170?cb=20200404154438']

    embed = discord.Embed(title="Random Loadout", colour=discord.Colour.blue(), timestamp=ctx.message.created_at)
    embed.set_image(url=f'{random.choice(weapon)}')
    embed.set_thumbnail(url=f'{random.choice(pistol)}')
    await ctx.send(embed=embed)

@client.command()
async def agent(ctx):
    agent = ['https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt53405c26141beff8/5f21fda671ec397ef9bf0894/V_AGENTS_587x900_KillJoy_.png',
            'https://static.wikia.nocookie.net/valorant_esports_gamepedia_en/images/c/ce/Agent_Jett_Half.png/revision/latest?cb=20200810060927',
            'https://static.wikia.nocookie.net/valorant/images/5/5c/Breach_artwork.png/revision/latest?cb=20200602020225',
            'https://static.wikia.nocookie.net/valorant/images/3/37/Brimstone_artwork.png/revision/latest?cb=20200602020239',
            'https://static.wikia.nocookie.net/valorant/images/f/fa/Phoenix_artwork.png/revision/latest?cb=20200602020246',
            'https://static.wikia.nocookie.net/valorant/images/0/06/Omen_artwork.png/revision/latest?cb=20200602020233',
            'https://static.wikia.nocookie.net/valorant/images/b/bb/Cypher_artwork.png/revision/latest?cb=20200602020329',
            'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c129aab8-0fed-4d3e-8c10-3fc467fb661b/ddyjdmr-b48faa53-4620-4de8-a2f9-77f168cc1ea6.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvYzEyOWFhYjgtMGZlZC00ZDNlLThjMTAtM2ZjNDY3ZmI2NjFiXC9kZHlqZG1yLWI0OGZhYTUzLTQ2MjAtNGRlOC1hMmY5LTc3ZjE2OGNjMWVhNi5wbmcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.S0m7CEbiSnXRJMBFdVs_7TVRkvz14Dr5XAzw-2hmygA',
            'https://static.wikia.nocookie.net/valorant/images/1/1e/Sage_artwork.png/revision/latest?cb=20200602020306',
            'https://static.wikia.nocookie.net/valorant/images/6/61/Sova_artwork.png/revision/latest?cb=20200602020314',
            'https://static.wikia.nocookie.net/valorant_esports_gamepedia_en/images/0/0a/Agent_Raze_Half.png/revision/latest?cb=20200810061659',
            'https://static.wikia.nocookie.net/valorant_esports_gamepedia_en/images/7/75/Agent_Viper_Half.png/revision/latest?cb=20200810061230',
            'https://static.wikia.nocookie.net/valorant/images/b/b9/Skye_Keyart_final.png/revision/latest?cb=20201013182515',
            'https://static.wikia.nocookie.net/valorant/images/a/a1/Yoru2.png/revision/latest?cb=20210112180407',
            'https://i2.wp.com/thegamehaus.com/wp-content/uploads/2021/01/Astra_KeyArt_Final.png?fit=779%2C1024&ssl=1']

    embed = discord.Embed(title="Random Agent", colour=discord.Colour.blue(), timestamp=ctx.message.created_at)
    embed.set_image(url=f'{random.choice(agent)}')
    await ctx.send(embed=embed)

@client.command()
async def avatar(ctx, *, member: discord.Member):

    embed = discord.Embed(colour=member.colour, timestamp=ctx.message.created_at)
    embed.set_author(name=f"Avatar of {member}")
    embed.set_image(url=member.avatar_url)
    
    await ctx.send(embed=embed)

@client.command()
async def insult(ctx, *, member: discord.Member=None):
    options = ['is a Noob',
            'is a Bot',
            'is Trash',
            'has small :brain:']
    await ctx.send(f'{member.mention} {random.choice(options)}')

@client.command()
async def hi(ctx, *args):
    for arg in args:
        await ctx.send(arg)

@client.command()
async def userinfo(ctx, *, member: discord.Member):

    roles = [role for role in member.roles]

    embed = discord.Embed(colour=member.colour,  timestamp=ctx.message.created_at)

    embed.set_author(name=f'User Info - {member}')
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text="Anshuman's Bot")

    embed.add_field(name="Joined Discord:", value=member.created_at.strftime("%a, %d %B %Y"), inline=False)
    embed.add_field(name="Joined Server:", value=member.joined_at.strftime("%a, %d %B %Y"), inline=False)

    embed.add_field(name='Bot?', value=member.bot, inline=False)

    embed.add_field(name=f'Roles ({len(roles)})', value='**|**'.join([role.mention for role in roles]), inline=False)

    await ctx.send(embed=embed)

@client.command()
async def punch(ctx, *, member: discord.Member):

    punch = ['https://media.giphy.com/media/GRM7Z2s6AougoR3rvv/giphy.gif',
            'https://media.giphy.com/media/1Bgr0VaRnx3pCZbaJa/giphy.gif',
            'https://media.giphy.com/media/xUO4t2gkWBxDi/giphy.gif',
            'https://media.giphy.com/media/ZcINp0p8P3vE4LAfLj/giphy.gif',
            'https://media.giphy.com/media/p3n74HP7NfrHO/giphy.gif']

    embed = discord.Embed(description = f'{ctx.author.mention} Punched {member.mention}', colour=discord.Colour.blue(), timestamp=ctx.message.created_at, inline=False)
    embed.set_image(url = f"{random.choice(punch)}")

    await ctx.send(embed=embed)

@client.command()
async def kick(ctx, *, member: discord.Member):

    kick = ['https://media.giphy.com/media/ujGq75KELBkffmo0RW/giphy.gif',
            'https://media.giphy.com/media/qiiimDJtLj4XK/giphy.gif',
            'https://media.giphy.com/media/l2QE2CQyK2ZyVEGJy/giphy.gif',
            'https://media.giphy.com/media/kDwKAjmtRpO9RTLcHq/giphy.gif',
            'https://media.giphy.com/media/FsoJPj4j0xpPG/giphy.gif',
            'https://media.giphy.com/media/mFulmRSjkW9by/giphy.gif']

    embed = discord.Embed(description = f'{ctx.author.mention} Kicked {member.mention}', colour=discord.Colour.blue(), timestamp=ctx.message.created_at, inline=False)
    embed.set_image(url=f"{random.choice(kick)}")

    await ctx.send(embed=embed)

@client.command()
async def hug(ctx, *, member: discord.Member):

    stab = ['https://media.giphy.com/media/yidUzriaAGJbsxt58k/giphy.gif ',
            'https://media.giphy.com/media/f6y4qvdxwEDx6/giphy.gif',
            'https://media.giphy.com/media/VduFvPwm3gfGO8duNN/giphy.gif',
            'https://media.giphy.com/media/xT1XGQve0LxCblDLr2/giphy.gif',
            'https://media.giphy.com/media/od5H3PmEG5EVq/giphy.gif',
            'https://media.giphy.com/media/yziFo5qYAOgY8/giphy.gif',
            'https://media.giphy.com/media/sUIZWMnfd4Mb6/giphy.gif',
            'https://media.giphy.com/media/ZQN9jsRWp1M76/giphy.gif']

    embed = discord.Embed(description = f'{ctx.author.mention} Hugged {member.mention}', colour=discord.Colour.blue(), timestamp=ctx.message.created_at, inline=False)
    embed.set_image(url=f"{random.choice(stab)}")

    await ctx.send(embed=embed)

@client.command()
async def pat(ctx, *, member: discord.Member):

    stab = ['https://media.giphy.com/media/5tmRHwTlHAA9WkVxTU/giphy.gif',
            'https://media.giphy.com/media/L2z7dnOduqEow/giphy.gif',
            'https://media.giphy.com/media/osYdfUptPqV0s/giphy.gif',
            'https://media.giphy.com/media/109ltuoSQT212w/giphy.gif',
            'https://media.giphy.com/media/wsUtKcUSHEhhBCyqtM/giphy.gif']

    embed = discord.Embed(description = f'{ctx.author.mention} Patted {member.mention}', colour=discord.Colour.blue(), timestamp=ctx.message.created_at, inline=False)
    embed.set_image(url=f"{random.choice(stab)}")

    await ctx.send(embed=embed)

@client.command()
async def stab(ctx, *, member: discord.Member):

    stab = ['https://media.giphy.com/media/xUySTCy0JHxUxw4fao/giphy.gif',
            'https://media.giphy.com/media/3o6ozCytqK9iZYgoVO/giphy.gif',
            'https://media.giphy.com/media/8cyqS8aTmUdHHbuoGm/giphy.gif',
            'https://media.giphy.com/media/lnakxcfG2MFy/giphy.gif',
            'https://media.giphy.com/media/RLJALCSN7lO4ctovsi/giphy.gif',]

    embed = discord.Embed(description = f'{ctx.author.mention} Stabbed {member.mention}', colour=discord.Colour.blue(), timestamp=ctx.message.created_at, inline=False)
    embed.set_image(url=f"{random.choice(stab)}")

    await ctx.send(embed=embed)

@client.command()
async def kidnap(ctx, *, member: discord.Member):

    kidnap = ['https://media.giphy.com/media/SaFGvUZAI7stfIfzRi/giphy.gif',
                'https://media.giphy.com/media/fSS3iKO07nArXJYeHs/giphy.gif',
                'https://media.giphy.com/media/3orif41pxhN6lAjtza/giphy.gif',
                'https://media.giphy.com/media/J0D3SVuQAQqD8BSuAL/giphy.gif',
                'https://media.giphy.com/media/PAbP0kXq6qDmCFWjHp/giphy.gif',
                'https://media.giphy.com/media/1dMLC2puOUhC52dyb3/giphy.gif']

    embed = discord.Embed(description = f'{ctx.author.mention} Kidnapped {member.mention}', colour=discord.Colour.blue(), timestamp=ctx.message.created_at, inline=False)
    embed.set_image(url=f"{random.choice(kidnap)}")

    await ctx.send(embed=embed)

@client.command()
async def slap(ctx, *, member: discord.Member):

    slap = ['https://media.giphy.com/media/Gf3AUz3eBNbTW/giphy.gif',
            'https://media.giphy.com/media/xUNd9HZq1itMkiK652/giphy.gif',
            'https://media.giphy.com/media/9U5J7JpaYBr68/giphy.gif',
            'https://media.giphy.com/media/VTVkjiRwO4LgA/giphy.gif',
            'https://media.giphy.com/media/srD8JByP9u3zW/giphy.gif',
            'https://media.giphy.com/media/Zau0yrl17uzdK/giphy.gif',
            'https://media.giphy.com/media/mEtSQlxqBtWWA/giphy.gif']

    embed = discord.Embed(description = f'{ctx.author.mention} Slapped {member.mention}', colour=discord.Colour.blue(), timestamp=ctx.message.created_at, inline=False)
    embed.set_image(url=f"{random.choice(slap)}")

    await ctx.send(embed=embed)

@client.command()
async def poll(ctx, *, message):
    embed = discord.Embed(title="POLL", description=f"{message}", colour=discord.Colour.blue())
    msg=await ctx.channel.send(embed=embed)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')

@client.command()
async def rate(ctx):
    embed = discord.Embed(title="Rate", description="Press the number you want to rate me", colour=discord.Colour.blue())
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/828496885647933471/6ee0758c3b9c229ffd3fd18e07991a40.webp?size=1024')
    msg=await ctx.channel.send(embed=embed)
    await msg.add_reaction('1️⃣')
    await msg.add_reaction('2️⃣')
    await msg.add_reaction('3️⃣')
    await msg.add_reaction('4️⃣')
    await msg.add_reaction('5️⃣')

def su(x:float,y:float):
    return x-y
def ad(x:float,y:float):
    return x+y
def di(x:float,y:float):
    return x/y
def mul(x:float,y:float):
    return x*y

@client.command()
async def add(ctx,x:float,y:float):
    res=ad(x,y)
    await ctx.send(res)

@client.command()
async def sub(ctx,x:float,y:float):
    res=su(x,y)
    await ctx.send(res)

@client.command()
async def div(ctx,x:float,y:float):
    res=di(x,y)
    await ctx.send(res)

@client.command()
async def multi(ctx,x:float,y:float):
    res=mul(x,y)
    await ctx.send(res)


@client.command()
async def status(ctx, *, member: discord.Member):
    embed = discord.Embed(colour=discord.Colour.blue())
    embed.add_field(name="Current Status:", value=str(member.status).title())

    await ctx.send(embed=embed)

@client.command()
async def rando(ctx):
    embed = discord.Embed(title = "Random Number", description = (random.randint(1, 101)), color = (0xF85252))
    embed.set_thumbnail(url='https://i.pinimg.com/originals/24/96/3b/24963bfad3386b063b9b0bcc5b42b089.jpg')
    await ctx.send(embed = embed)

@client.command()
async def temp(ctx):
    embed = discord.Embed(title = "Temperature(in °C)", description = (random.randint(18, 30)), color = (0xF85252))
    embed.set_thumbnail(url='https://i.pinimg.com/originals/06/c4/f7/06c4f70ec5931e2342e703e8a3f0a253.png')
    embed.set_footer(text='(fake)')
    await ctx.send(embed = embed)

@client.command()
async def dm(ctx, member: discord.Member, *, msg):
    await ctx.send(f'Successfully sent to {member.mention}')
    await member.send(msg)

@client.command()
async def dm_all(ctx, *, msg=None):
    if msg != None:
        members = ctx.guild.members
        for member in members:
            try:
                await member.send(msg)
            except:
                print("")
    else:
        await ctx.send("Syntax = .dm_all (message)")
    
@client.command()
async def define(ctx, *, sth):
    await ctx.send(wikipedia.summary(sth, sentences=2))

@client.command()
async def scream(ctx):
    await ctx.send('AAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHH')

@client.command()
async def rr(ctx, *, member: discord.Member):

    rr = ['https://media.giphy.com/media/10kABVanhwykJW/giphy.gif']

    embed = discord.Embed(description = f'{ctx.author.mention} Rickrolled {member.mention}', colour=discord.Colour.blue(), timestamp=ctx.message.created_at, inline=False)
    embed.set_image(url=f"{random.choice(rr)}")

    await ctx.send(embed=embed)

@client.command()
async def jett_info(ctx):
    embed = discord.Embed(title = 'Jett', description = 'Duelist', colour = discord.Colour.blue(), timestamp = ctx.message.created_at)
    embed.set_image(url='https://static.wikia.nocookie.net/valorant_esports_gamepedia_en/images/c/ce/Agent_Jett_Half.png/revision/latest/scale-to-width-down/391?cb=20200810060927')
    embed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/4/4f/Spray_Jett.png/revision/latest/scale-to-width-down/512?cb=20200805074112')
    embed.add_field(name = "Nationality", value = "Korean")
    embed.add_field(name = "Abilities", value = "Tailwind,Updraft,Cloudburst,Blade Storm")
    embed.add_field(name = "Tailwind(E)", value = "Cost = Free\nDash range = 15m", inline=False)
    embed.add_field(name = "Updraft(Q)", value = "Cost = 100\nVertical range = 5m", inline=False)
    embed.add_field(name = "Cloudburst(C)", value = "Cost = 100\n Duration = 7s", inline=False)
    embed.add_field(name = "Blade Storm(X)", value = "Cost = 6 kills\nDamage = 50\nKnives = 5(refreshes on kill)", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def phoenix_info(ctx):
    embed = discord.Embed(title = 'Phoenix', description = 'Duelist', colour = discord.Colour.blue(), timestamp = ctx.message.created_at)
    embed.set_image(url='https://static.wikia.nocookie.net/valorant_esports_gamepedia_en/images/9/97/Agent_Phoenix_Half.png/revision/latest/scale-to-width-down/391?cb=20200810061618')
    embed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/d/dc/Spray_Phoenix.png/revision/latest/scale-to-width-down/512?cb=20200805125235')
    embed.add_field(name = "Nationality", value = "British")
    embed.add_field(name = "Abilities", value = "Hot Hands,Curveball,Cloudburst,Run it back")
    embed.add_field(name = "Hot Hands(E)", value = "Cost = Free\nDuration = 4s, Heal = 1 HP/0.08s\nDamage = 15/0.25s", inline=False)
    embed.add_field(name = "CurveBall(Q)", value = "Cost = 200,\nFlash duration = 1.75s", inline=False)
    embed.add_field(name = "Blaze(C)", value = "Cost = 200\nDuration = 8s\nHeal = 1 HP/0.16s\nDamage = 1/0.033s", inline=False)
    embed.add_field(name = "Run it Back(X)", value = "Cost = 6 kills\nDuration = 10s", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def breach_info(ctx):
    embed = discord.Embed(title = 'Breach', description = 'Initiator', colour = discord.Colour.blue(), timestamp = ctx.message.created_at)
    embed.set_image(url='https://static.wikia.nocookie.net/valorant_esports_gamepedia_en/images/d/de/Agent_Breach_Half.png/revision/latest/scale-to-width-down/391?cb=20200810061334')
    embed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/8/82/Spray_Breach.png/revision/latest/scale-to-width-down/512?cb=20200805114029')
    embed.add_field(name = "Nationality", value = "Swedish")
    embed.add_field(name = "Abilities", value = "Fault Line,Flashpoint,Aftershock,Rolling Thunder")
    embed.add_field(name = "Fault Line(E)", value = "Cost = Free\nDaze duration = 3s\nRange = 10 - 50m", inline=False)
    embed.add_field(name = "Flashpoint(Q)", value = "Cost = 200\nFlash duration = 1s - 2s\nFlash delay = 0.5s", inline=False)
    embed.add_field(name = "Aftershock(C)", value = "Cost = 100\nDelay = 2.2s\nDamage = 60 - 175", inline=False)
    embed.add_field(name = "Rolling Thunder(X)", value = "Cost = 7 kills\nDaze duration = 6s\nRange = 38m", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def astra_info(ctx):
    embed = discord.Embed(title = 'Astra', description = 'Controller', colour = discord.Colour.blue(), timestamp = ctx.message.created_at)
    embed.set_image(url='https://liquipedia.net/commons/images/1/13/Astra_Artwork.png')
    embed.set_thumbnail(url='https://cdn.valorantinfo.gg/img/sprays/Astra.png')
    embed.add_field(name = "Nationality", value = "Ghanaian")
    embed.add_field(name = "Abilities", value = "Nebula,Nova Pulse,Gravity Well,Cosmic Divide")
    embed.add_field(name = "Nebula(E)", value = "Cost = 200\nFormation = 0.5s\nSmoke duration = 15s\nDissipate duration = 2s", inline=False)
    embed.add_field(name = "Nova Pulse(Q)", value = "Cost = 200\nCharge time = 1s\nDaze duration = 4s", inline=False)
    embed.add_field(name = "Gravity Well(C)", value = "Cost = 200\nPull duration = 3s\nVulnerable duration = 5s", inline=False)
    embed.add_field(name = "Cosmic Divide(X)", value = "Cost = 7 kills\nActivation time = 3s\nDuration = 20s", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def brimstone_info(ctx):
    embed = discord.Embed(title = 'Brimstone', description = 'Controller', colour = discord.Colour.blue(), timestamp = ctx.message.created_at)
    embed.set_image(url='https://static.wikia.nocookie.net/valorant_esports_gamepedia_en/images/9/91/Agent_Brimstone_Half.png/revision/latest/scale-to-width-down/391?cb=20200810061420')
    embed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/4/4e/Spray_Brimstone.png/revision/latest/scale-to-width-down/512?cb=20200805125226')
    embed.add_field(name = "Nationality", value = "American")
    embed.add_field(name = "Abilities", value = "Sky Smoke,Incendiary,Stim Beacon,Orbital Strike")
    embed.add_field(name = "Sky Smoke(E)", value = "Cost = 100\nDuration = 19s\nExpansion duration = 0.75\nLanding delay = 2s", inline=False)
    embed.add_field(name = "Incendiary(Q)", value = "Cost = 300\nDuration = 8s\nDamage = 15 per 0.25s", inline=False)
    embed.add_field(name = "Stim Beacon(C)", value = "Cost = 100\nDuration = 12s\nEffect = increased reload\nequip speed\naim recovery", inline=False)
    embed.add_field(name = "Orbital Strike(X)", value = "Cost = 7 kills\nDuration = 4s\nDamage = 20 per 0.16s\nDelay = 2s", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def cypher_info(ctx):
    embed = discord.Embed(title = 'Cypher', description = 'Sentinel', colour = discord.Colour.blue(), timestamp = ctx.message.created_at)
    embed.set_image(url='https://static.wikia.nocookie.net/valorant_esports_gamepedia_en/images/a/a0/Agent_Cypher_Half.png/revision/latest/scale-to-width-down/391?cb=20200810061139')
    embed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/7/79/Spray_Cypher.png/revision/latest/scale-to-width-down/512?cb=20200805125227')
    embed.add_field(name = "Nationality", value = "Moroccan")
    embed.add_field(name = "Abilities", value = "Spycam,Cyber Cage,Trapwire,Neural Theft")
    embed.add_field(name = "Spycam(E)", value = "Cost = Free\nCooldown for dart = 6s\nEffect = Pings enemy location every 2s", inline=False)
    embed.add_field(name = "Cyber Cage(Q)", value = "Cost = 100\nDuration = 7s\nStealth delay = 1.4s", inline=False)
    embed.add_field(name = "Trapwire(C)", value = "Cost = 200\nReveal duration = 3s\nDaze duration = 3s\nDamage = 5", inline=False)
    embed.add_field(name = "Neural Theft(X)", value = "Cost = 7 kills\nCast range = 12m\nUpload time = 2s\nFresh corpse duration = 20s", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def killjoy_info(ctx):
    embed = discord.Embed(title = 'Killjoy', description = 'Sentinal', colour = discord.Colour.blue(), timestamp = ctx.message.created_at)
    embed.set_image(url='https://static.wikia.nocookie.net/valorant_esports_gamepedia_en/images/6/68/Agent_Killjoy_Half.png/revision/latest/scale-to-width-down/391?cb=20200805115349')
    embed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/5/5e/Spray_Killjoy.png/revision/latest/scale-to-width-down/512?cb=20200805125232')
    embed.add_field(name = "Nationality", value = "German")
    embed.add_field(name = "Abilities", value = "Turret,Alarmbot,Nanoswarm,Lockdown")
    embed.add_field(name = "Turret(E)", value = "Cost = Free\nHealth = 125 HP\n0-20m = 8 dmg per bullet, 20-35m = 6 dmg per bullet, 35m+ = 4 dmg per bullet\nCooldown = 10s,\nDeactivation range = 40m", inline=False)
    embed.add_field(name = "Alarmbot(Q)", value = "Cost = 200\nDebuff duration = 4s\nDetection range = 7m\nCooldown = 7s\nDeactivation range = 40m", inline=False)
    embed.add_field(name = "Nanoswarm(C)", value = "Cost = 200\nDuration = 4.5s\nDamage = 45/s", inline=False)
    embed.add_field(name = "Lockdown(X)", value = "Cost = 7 kills\nHealth = 150 HP\nCountdown = 13s\nDebuff duration = 8s", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def omen_info(ctx):
    embed = discord.Embed(title = 'Omen', description = 'Controller', colour = discord.Colour.blue(), timestamp = ctx.message.created_at)
    embed.set_image(url='https://static.wikia.nocookie.net/valorant_esports_gamepedia_en/images/6/68/Agent_Omen_Half.png/revision/latest/scale-to-width-down/391?cb=20200810061546')
    embed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/f/f9/Spray_Omen.png/revision/latest/scale-to-width-down/512?cb=20200805103844')
    embed.add_field(name = "Nationality", value = "Unknown")
    embed.add_field(name = "Abilities", value = "Dark Cover,Paranoia,Shrouded Step,From the Shadows")
    embed.add_field(name = "Dark Cover(E)", value = "Cost = Free\nDuration = 15s\nRange = 80m", inline=False)
    embed.add_field(name = "Paranoia(Q)", value = "Cost = 400\nNearsight duration = 2.5s\nRange = 35m", inline=False)
    embed.add_field(name = "Shrouded Step(C)", value = "Cost = 100\nRange = 15m", inline=False)
    embed.add_field(name = "From the Shadows(X)", value = "Cost = 7 kills\nTotal cast time = 4s\nShade form = 2.5s\nReform time = 0.75s", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def raze_info(ctx):
    embed = discord.Embed(title = 'Raze', description = 'Duelist', colour = discord.Colour.blue(), timestamp = ctx.message.created_at)
    embed.set_image(url='https://static.wikia.nocookie.net/valorant_esports_gamepedia_en/images/0/0a/Agent_Raze_Half.png/revision/latest/scale-to-width-down/391?cb=20200810061659')
    embed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/8/82/Spray_Raze.png/revision/latest/scale-to-width-down/512?cb=20200805125238')
    embed.add_field(name = "Nationality", value = "Brazilian")
    embed.add_field(name = "Abilities", value = "Paint Shells,Blast Pack,Boom Bot,Showstopper")
    embed.add_field(name = "Paint Shells(E)", value = "Cost = Free\nDamage = 55\nFuse time = 2s", inline=False)
    embed.add_field(name = "Blast Pack(Q)", value = "Cost = 200\nDamage = 50\nDuration = 5s,\nMax damage range = 1m", inline=False)
    embed.add_field(name = "Boom Bot(C)", value = "Cost = 200\nDamage = 125\nDuration = 10s\nHealth = 100 HP", inline=False)
    embed.add_field(name = "Showstopper(X)", value = "Cost = 7 kills\nDamage = 150\nDuration = 10s\nEquip time = 1.4s", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def reyna_info(ctx):
    embed = discord.Embed(title = 'Reyna', description = 'Duelist', colour = discord.Colour.blue(), timestamp = ctx.message.created_at)
    embed.set_image(url='https://static.wikia.nocookie.net/valorant_esports_gamepedia_en/images/4/4a/Agent_Reyna_Half.png/revision/latest/scale-to-width-down/391?cb=20200629122204')
    embed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/b/bd/Spray_Reyna.png/revision/latest/scale-to-width-down/512?cb=20200806062741')
    embed.add_field(name = "Nationality", value = "Mexican")
    embed.add_field(name = "Abilities", value = "Dismiss,Devour,Leer,Empress")
    embed.add_field(name = "Dismiss(E)", value = "Cost = 200\nDuration = 2s", inline=False)
    embed.add_field(name = "Devour(Q)", value = "Cost = 200\nDuration = 3s\nHeal amount = 100 HP over 3 seconds\nOverheal duration = 25s", inline=False)
    embed.add_field(name = "Leer(C)", value = "Cost = 200\nDuration = 2s", inline=False)
    embed.add_field(name = "Empress(X)", value = "Cost = 6 kills\nDuration = 30s\nEffect = increased ROF\nincreased equip and reload speed", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def sage_info(ctx):
    embed = discord.Embed(title = 'Sage', description = 'Sentinal', colour = discord.Colour.blue(), timestamp = ctx.message.created_at)
    embed.set_image(url='https://static.wikia.nocookie.net/valorant_esports_gamepedia_en/images/d/d7/Agent_Sage_Half.png/revision/latest/scale-to-width-down/391?cb=20200810061753')
    embed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/9/99/Sage_Spray.png/revision/latest/scale-to-width-down/300?cb=20201113134232')
    embed.add_field(name = "Nationality", value = "Chinese")
    embed.add_field(name = "Abilities", value = "Heal Orb,Slow Orb,Barrier Orb,Resurrection")
    embed.add_field(name = "Heal Orb(E)", value = "Cost = Free\nDuration = 5s\nHeal speed = 12 HP/s\nHeal pause on hit = 2s\nHeal amount = 60 HP", inline=False)
    embed.add_field(name = "Slow Orb(Q)", value = "Cost = 100\nDuration = 7s\nMovement slow = 50%\nJump height reduction = 30%", inline=False)
    embed.add_field(name = "Barrier Orb(C)", value = "Cost = 300\nDuration = 30s\nHealth = 800HP per segment", inline=False)
    embed.add_field(name = "Resurrection(X)", value = "Cost = 7 kills\nInvulnerability duration = 2s", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def skye_info(ctx):
    embed = discord.Embed(title = 'Skye', description = 'Initiator', colour = discord.Colour.blue(), timestamp = ctx.message.created_at)
    embed.set_image(url='https://static.wikia.nocookie.net/valorant/images/b/b9/Skye_Keyart_final.png/revision/latest?cb=20201013182515')
    embed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/2/27/Skye_Spray.png/revision/latest/scale-to-width-down/700?cb=20201105175436')
    embed.add_field(name = "Nationality", value = "Australian")
    embed.add_field(name = "Abilities", value = "Guiding Light,Trailblazer,Regrowth,Seekers")
    embed.add_field(name = "Guiding Light(E)", value = "Cost = 100\nFlash duration = 1s - 3s\nFlight duration = 2.5s\nHealth = 60", inline=False)
    embed.add_field(name = "Trailblazer(Q)", value = "Cost = 200\nDuration = 6s\nDamage = 30\nEffect = 3s Daze on hit\nHealth = 100 HP", inline=False)
    embed.add_field(name = "Regrowth(C)", value = "Cost = 200\nTotal heal amount = 100\nHeal speed = 20 HP/s\nRadius = 1000", inline=False)
    embed.add_field(name = "Seekers(X)", value = "Cost = 6 kills\nNearsight duration = 3s\nHP = 150\nSearch duration = 15s", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def sova_info(ctx):
    embed = discord.Embed(title = 'Sova', description = 'Initiator', colour = discord.Colour.blue(), timestamp = ctx.message.created_at)
    embed.set_image(url='https://static.wikia.nocookie.net/valorant_esports_gamepedia_en/images/8/80/Agent_Sova_Half.png/revision/latest/scale-to-width-down/391?cb=20200810061819')
    embed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/2/2b/Spray_Sova.png/revision/latest/scale-to-width-down/512?cb=20200805125241')
    embed.add_field(name = "Nationality", value = "Russina")
    embed.add_field(name = "Abilities", value = "Recon Bolt,Shock Bolt,Owl Drone,Hunter's Fury")
    embed.add_field(name = "Recon Bolt(E)", value = "Cost = Free\nDuration = 5.625s\nReveal duration = 3s", inline=False)
    embed.add_field(name = "Shock Bolt(Q)", value = "Cost = 100\nDamage = 10-90", inline=False)
    embed.add_field(name = "Owl Drone(C)", value = "Cost = 300\nDuration = 10s\nHealth = 120 HP\nDart cooldown = 5s", inline=False)
    embed.add_field(name = "Hunter's Fury(X)", value = "Cost = 7 kills\nDamage = 80\nRange = 66m\nDuration = 6.5s", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def viper_info(ctx):
    embed = discord.Embed(title = 'Viper', description = 'Controller', colour = discord.Colour.blue(), timestamp = ctx.message.created_at)
    embed.set_image(url='https://static.wikia.nocookie.net/valorant_esports_gamepedia_en/images/7/75/Agent_Viper_Half.png/revision/latest/scale-to-width-down/391?cb=20200810061230')
    embed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/1/17/Spray_Viper.png/revision/latest/scale-to-width-down/512?cb=20200805125222')
    embed.add_field(name = "Nationality", value = "American")
    embed.add_field(name = "Abilities", value = "Toxic Screen,Poison Cloud,Snake Bite,Viper's Pit")
    embed.add_field(name = "Toxic Screen(E)", value = "Cost = Free\nMinimum fuel = 20\nCost = 5 Fuel/sec", inline=False)
    embed.add_field(name = "Poison Cloud(Q)", value = "Cost = 200\nMinimum fuel = 20\nCost = 5 Fuel/sec", inline=False)
    embed.add_field(name = "Snake Bite(C)", value = "Cost = 100\nDuration = 8s\nDamage = 1 per 0.04s", inline=False)
    embed.add_field(name = "Viper's Pit(X)", value = "Cost = 7 kills\nDuration outside before collapsing = 15s\nDecay drain = 50 instant, 10HP/s", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def yoru_info(ctx):
    embed = discord.Embed(title = 'Yoru', description = 'Duelist', colour = discord.Colour.blue(), timestamp = ctx.message.created_at)
    embed.set_image(url='https://static.wikia.nocookie.net/valorant/images/a/a1/Yoru2.png/revision/latest?cb=20210112180407')
    embed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/1/15/Yoru_Spray.png/revision/latest/scale-to-width-down/1000?cb=20210104055449')
    embed.add_field(name = "Nationality", value = "Japanese")
    embed.add_field(name = "Abilities", value = "Gatecrash,Blindside,Fakeout,Dimensional Drift")
    embed.add_field(name = "Gatecrash(E)", value = "Cost = Free\nDuration = 30s\nStealth range = 4m", inline=False)
    embed.add_field(name = "Blindside(Q)", value = "Cost = 200\nFlash duration = 1.5s", inline=False)
    embed.add_field(name = "Fakeout(C)", value = "Cost = 100\nDuration = 10s", inline=False)
    embed.add_field(name = "Dimensional Drift(X)", value = "Cost = 6 kills\nDuration = 9s\nDetection radius = 2.5m", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def yes(ctx):

    yes = ['https://media.giphy.com/media/sWlc4HHqhGHKwIKxj2/giphy.gif',
            'https://media.giphy.com/media/ckeHl52mNtoq87veET/giphy.gif']

    embed = discord.Embed(description = f'{ctx.author.mention} says yes', colour=discord.Colour.blue(), timestamp=ctx.message.created_at, inline=False)
    embed.set_image(url=f"{random.choice(yes)}")

    await ctx.send(embed=embed)

@client.command()
async def no(ctx):

    no = ['https://media.giphy.com/media/eKrgVyZ7zLvJrgZNZn/giphy.gif',
            'https://media.giphy.com/media/26hkhKd2Cp5WMWU1O/giphy.gif']

    embed = discord.Embed(description = f'{ctx.author.mention} says no', colour=discord.Colour.blue(), timestamp=ctx.message.created_at, inline=False)
    embed.set_image(url=f"{random.choice(no)}")

    await ctx.send(embed=embed)

@client.command()
async def gm(ctx, *, member: discord.Member):
    await ctx.send(f'{member.mention}, {ctx.author.mention} says Good Morning')

@client.command()
async def ga(ctx, *, member: discord.Member):
    await ctx.send(f'{member.mention}, {ctx.author.mention} says Good Afernoon')

@client.command()
async def gn(ctx, *, member: discord.Member):
    await ctx.send(f'{member.mention}, {ctx.author.mention} says Good Night')

@client.command()
async def gd(ctx, *, member: discord.Member):
    await ctx.send(f'{member.mention}, {ctx.author.mention} says Good Day')

@client.command()
async def giveaway(ctx, *, prize : str):
    embed = discord.Embed(title = "Giveaway", description = f'{prize}', colour = discord.Colour.red(), timestamp = ctx.message.created_at)

    users = ctx.guild.members
    user1 = choice(users)

    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/823801109092237335/829381213542154340/giveaway.png')
    embed.add_field(name = "Hosted by", value = f"{ctx.author.mention}")
    embed.add_field(name = "Winner", value = f"{user1.mention}", inline=False)

    await ctx.send(embed=embed)
    await ctx.send(f"Congrats {user1.mention} on winning **{prize}**")

@client.command()
async def spam(ctx, *,message):
    while True:
        await ctx.send(f'{message}')

@client.command()
async def cube(ctx):
    embed = discord.Embed(title = "Cube Formulae", colour = discord.Colour.blurple(), timestamp = ctx.message.created_at)
    embed.set_thumbnail(url="https://cdn-skill.splashmath.com/panel-uploads/GlossaryTerm/7017ed7b14c14daf85c7fd14d5d38291/1548234334_cube.png")
    embed.add_field(name = "TSA", value = "6a²", inline=False)
    embed.add_field(name = "LSA", value = "4a²", inline=False)
    embed.add_field(name = "Volume", value = "a³", inline=False)

    await ctx.send(embed=embed)

@client.command()
async def cuboid(ctx):
    embed = discord.Embed(title = "Cuboid Formulae", colour = discord.Colour.blurple(), timestamp = ctx.message.created_at)
    embed.set_thumbnail(url="https://cdn-skill.splashmath.com/panel-uploads/GlossaryTerm/7017ed7b14c14daf85c7fd14d5d38291/1548234334_rectangular-prism.png")
    embed.add_field(name = "TSA", value = "2(lb+bh+hl)", inline=False)
    embed.add_field(name = "LSA", value = "2h(l+b)", inline=False)
    embed.add_field(name = "Volume", value = "lbh", inline=False)

    await ctx.send(embed=embed)

@client.command()
async def sphere(ctx):
    embed = discord.Embed(title = "Sphere Formulae", colour = discord.Colour.blurple(), timestamp = ctx.message.created_at)
    embed.set_thumbnail(url="https://cdn-skill.splashmath.com/panel-uploads/GlossaryTerm/7017ed7b14c14daf85c7fd14d5d38291/1548234334_sphere.png")
    embed.add_field(name = "TSA", value = "4πr²", inline=False)
    embed.add_field(name = "Volume", value = "4/3 πr³", inline=False)

    await ctx.send(embed=embed)

@client.command()
async def hemisphere(ctx):
    embed = discord.Embed(title = "Hemisphere Formulae", colour = discord.Colour.blurple(), timestamp = ctx.message.created_at)
    embed.set_thumbnail(url="https://res.cloudinary.com/dk-find-out/image/upload/q_80,w_960,f_auto/hemisphere_rfwgde.jpg")
    embed.add_field(name = "TSA", value = "3πr²", inline=False)
    embed.add_field(name = "Volume", value = "2/3 πr³", inline=False)

    await ctx.send(embed=embed)

@client.command()
async def cone(ctx):
    embed = discord.Embed(title = "Cone Formulae", colour = discord.Colour.blurple(), timestamp = ctx.message.created_at)
    embed.set_thumbnail(url="https://cdn-skill.splashmath.com/panel-uploads/GlossaryTerm/7017ed7b14c14daf85c7fd14d5d38291/1548234334_cone.png")
    embed.add_field(name = "TSA", value = "πr(r+l)", inline=False)
    embed.add_field(name = "LSA", value = "πr√(r²+h²)", inline=False)
    embed.add_field(name = "Volume", value = "πr² h/3", inline=False)

    await ctx.send(embed=embed)

@client.command()
async def cylinder(ctx):
    embed = discord.Embed(title = "Cylinder Formulae", colour = discord.Colour.blurple(), timestamp = ctx.message.created_at)
    embed.set_thumbnail(url="https://cdn-skill.splashmath.com/panel-uploads/GlossaryTerm/7017ed7b14c14daf85c7fd14d5d38291/1548234334_cylinder.png")
    embed.add_field(name = "TSA", value = "2πr(r+h)", inline=False)
    embed.add_field(name = "LSA", value = "2πrh", inline=False)
    embed.add_field(name = "Volume", value = "πr²h", inline=False)

    await ctx.send(embed=embed)

@client.command()
async def trigno(ctx):
    embed = discord.Embed(title = "Trigonometric Ratios", colour = discord.Colour.dark_orange(), timestamp = ctx.message.created_at)
    embed.set_image(url="https://i.pinimg.com/originals/aa/94/66/aa9466eb061bd5255eadb470d3a42c8c.gif")
    
    await ctx.send(embed=embed)

@client.command()
async def about(ctx):
    embed = discord.Embed(title = "About the developer", colour = discord.Colour.green(), timestamp = ctx.message.created_at)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/702137359122169976/93c66338aa05a61f38d25dfcecd3a512.webp?size=1024")
    embed.add_field(name = "Name", value = "Anshuman Bhardwaj", inline=False)
    embed.add_field(name = "Discord", value = "MrAnshuman #1060", inline=False)
    embed.add_field(name = "Gmail", value = "abtbbruv@gmail.com", inline=False)
    embed.add_field(name = "Bot Server", value = "https://discord.gg/TtByRnt82F", inline=False)

    await ctx.send(embed=embed)

@client.command(aliases=['jokes'])
async def joke(ctx):
    await ctx.send(pyjokes.get_joke())

@client.command()
async def info(ctx):
    embed = discord.Embed(title = "About the bot", colour = discord.Colour.green(), timestamp = ctx.message.created_at)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/828496885647933471/6ee0758c3b9c229ffd3fd18e07991a40.webp?size=1024")
    embed.add_field(name = "Name", value = "Anshuman's Bot", inline=False)
    embed.add_field(name = "Prefix", value = ".", inline=False)
    embed.add_field(name = "Created at", value = "Mon, 05 April 2021", inline=False)
    embed.add_field(name = "Bot Server", value = "https://discord.gg/TtByRnt82F", inline=False)

    await ctx.send(embed=embed)

@client.command()
async def report(ctx, member: discord.Member, *, reason):
    embed = discord.Embed(title = "Caution", colour = discord.Colour.dark_teal())
    embed.set_thumbnail(url='https://www.ifhomeless.org/wp-content/uploads/2017/01/caution-yellow-noborer-500x435.png')
    embed.add_field(name = "Reporter", value = f"{ctx.author.mention}", inline=False)
    embed.add_field(name = "Target", value = f"{member.mention}", inline=False)
    embed.add_field(name = "Reason", value = f"{reason}")

    await ctx.send(embed=embed)

@client.command()
async def refraction(ctx):
    embed = discord.Embed(title = "Refraction of Light",
                            description = "The change in direction of light when it passes from one optical medium to another is called refraction of light.",
                            colour = discord.Colour.greyple(),
                            timestamp = ctx.message.created_at)

    embed.set_image(url='https://upload.wikimedia.org/wikipedia/commons/8/85/Refraction_photo.png')
    embed.add_field(name = "Law 1", value = "The incident ray, refracted ray and normal to the interface of two transparent media at the point of incidence, all lie in the same plane.")
    embed.add_field(name = "Law 2", value = "The ratio of sine of angle of incidence to the sine of angle of refraction is a constant for the given pair of medium and for a given colour of light.")

    await ctx.send(embed=embed)

@client.command()
async def reflection(ctx):
    embed = discord.Embed(title = "Reflection of Light",
                            description = "The bouncing back of light rays into the same medium after striking the surface a highly polished opaque object like mirror.",
                            colour = discord.Colour.greyple(),
                            timestamp = ctx.message.created_at)

    embed.set_image(url='https://www.scienceabc.com/wp-content/uploads/2018/11/law-of-reflection.jpg')
    embed.add_field(name = "Law 1", value = "The angle of incidence is equal to angle of reflection. ")
    embed.add_field(name = "Law 2", value = "The incident ray, the reflected ray and the normal at the point of incidence, all lie in the same plane.")

    await ctx.send(embed=embed)

@client.command()
async def tell(ctx, *, say):
    await ctx.send(f'{say}')

@client.command()
async def timer(ctx, seconds):
    try:
        secondint = int(seconds)
        if secondint >= 3600:
            await ctx.send("I cant set a timer for more than 1 hour")
            raise BaseException
        
        if secondint <= 0:
            await ctx.send("I cant set a timer less than 0 seconds")
            raise BaseException

        message = await ctx.send(f"Timer: {seconds}")

        while True:
            secondint -= 1
            if secondint == 0:
                await message.edit(content="Ended")
                break

            await message.edit(content=f"Timer: {secondint}")
            await asyncio.sleep(1)
        await ctx.send(f"{ctx.author.mention}, Your timer has ended!")
    except ValueError:
        await ctx.send("You must enter a number!")

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send(f"Joined {channel}")

@client.command()
async def leave(ctx):
    channel = ctx.author.voice.channel
    await ctx.voice_client.disconnect()
    await ctx.send(f"Left {channel}")

@client.command()
async def wallpaper(ctx):
    
    wallpapers = ['https://cdn.discordapp.com/attachments/823801109092237335/830700952445124658/4k_3.jpg',
                    'https://cdn.discordapp.com/attachments/823801109092237335/830700952607653938/4k_1.jpg',
                    'https://cdn.discordapp.com/attachments/823801109092237335/830700955272085504/4k_wallpaper.jpg',
                    'https://cdn.discordapp.com/attachments/823801109092237335/830700955447197746/digital-art-fantasy-art-total-war-warhammer-trees-wallpaper-preview.jpg',
                    'https://cdn.discordapp.com/attachments/823801109092237335/830700960124108820/hill_wallpaper.jpg',
                    'https://cdn.discordapp.com/attachments/823801109092237335/830700965107073074/lake_tree.png',
                    'https://cdn.discordapp.com/attachments/823801109092237335/830700965204066324/valley-90388_1920.jpg',
                    'https://cdn.discordapp.com/attachments/823801109092237335/830700966382534666/nature-5025558_1920.jpg',
                    'https://wallpaperaccess.com/full/43654.jpg',
                    'https://wallpaper.dog/large/443.png',
                    'https://wallpaperaccess.com/full/345330.jpg',
                    'https://wallpaperaccess.com/full/660691.jpg',
                    'https://www.desktopbackground.org/download/2560x1440/2010/09/18/82050_nature-4k-ultra-hd-wallpapers-4k-wallpaper-net_2560x1600_h.jpg']

    embed = discord.Embed(title = "Wallpaper", colour = discord.Colour.red(), timestamp = ctx.message.created_at)
    embed.set_image(url=f'{random.choice(wallpapers)}')

    await ctx.send(embed=embed)

@client.command()
async def td(ctx):

    truth_items = ["If you could be invisible, what is the first thing you would do?",
                "What's your biggest regret?",
                "If a genie granted you three wishes, what would you ask for",
                "When was the last time you lied?",
                "What animal do you think you most look like?",
                "What's your biggest fear?",
                "What's your worst habit?",
                "How many stuffed animals do you own?",
                "Do you have a hidden talent?",
                "Have you ever broken the law?",
                "What's the biggest mistake you've ever made?",
                "What's the worst thing you've lied about?",
                "Do you have a favourite friend?",
                "Do you have a favourite song?",
                "What's the strangest rumour you've heard about yourself?",
                "What's the most trouble you've been in?"]

    dare_items = ["Let another person decide a your discord status.",
            "Eat a bite of a banana peel.",
            "Imitate a YouTuber until another player guesses who you are portraying.",
            "Call a friend, pretend it's their birthday, and sing them Happy Birthday to You.",
            "Play air guitar for one minute.",
            "Do 20 squats right now.",
            "Do a prank call on one of your family members.",
            "Keep three ice cubes in your mouth until they melt.",
            "Eat a spoonful of mustard.",
            "Let the group look in your Instagram DMs.",
            "Try to lick your elbow.",
            "Say everything in a whisper for the next 10 minutes.",
            "Dance without music for two minutes.",
            "Tell the saddest story you know",
            "Try and make yourself cry in front of the group."]

    await ctx.send("please type **t** for truth and **d** for dare")
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() in ("t", "d")
    message = await client.wait_for("message", check=check)
    choice = message.content.lower()
    if choice == "t":
        await ctx.send(f"{random.choice(truth_items)}")
    if choice == "d":
        await ctx.send(f"{random.choice(dare_items)}")

@client.command()
async def ref_index(ctx):
    embed = discord.Embed(title = "Refractive Index", colour = discord.Colour.dark_orange(), timestamp = ctx.message.created_at)
    embed.set_image(url="https://d1avenlh0i1xmr.cloudfront.net/be663778-24d5-42a9-86d5-3be713baf1e1/table-10.3-ncert---refractive-index-of-some-media.jpg")
    
    await ctx.send(embed=embed)

@client.command()
async def reminder(ctx, seconds, *, reason):
    try:
        secondint = int(seconds)
        if secondint >= 3600:
            await ctx.send("I cant set a timer for more than 1 hour")
            raise BaseException
        
        if secondint <= 0:
            await ctx.send("I cant set a timer less than 0 seconds")
            raise BaseException

        message = await ctx.send(f"Timer: {seconds}")

        while True:
            secondint -= 1
            if secondint == 0:
                await message.edit(content="Ended")
                break

            await message.edit(content=f"Timer: {secondint}")
            await asyncio.sleep(1)
        await ctx.send(f"{ctx.author.mention}, ***REMINDER!***    **{reason}**")
    except ValueError:
        await ctx.send("You must enter a number!")
        
@client.command()
async def fox(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/fox')
      foxjson = await request.json()
      
      request2 = await session.get('https://some-random-api.ml/facts/fox')
      factjson = await request2.json()

   embed = discord.Embed(title="Fox", color=discord.Color.random())
   embed.set_image(url=foxjson['link'])
   embed.set_footer(text=factjson['fact'])
   
   await ctx.send(embed=embed)

@client.command(aliases=['cmd', 'cmds'])
async def commands(ctx):
    embed = discord.Embed(
        title = 'Help',
        description = 'Prefix .\nUse .commands/.cmds/.cmd to open this\nUse .about to know about the developer\nUse .info to know about the bot',
        color = discord.Color.blue()
    )

    embed.set_footer(text='Bot by MrAnshuman#1060')
    embed.set_image(url='https://cdn.discordapp.com/attachments/828339543514021902/830516904183070730/Bot_pfp_2.jpg')
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/828496885647933471/6ee0758c3b9c229ffd3fd18e07991a40.webp?size=1024')
    embed.add_field(name = "Moderation", value = "kick_server,ban,    unban,delete")
    embed.add_field(name = "Fun", value = "ping,toss,roll,   insult,hi,    scream,joke,  tell,td")
    embed.add_field(name = "Information", value = "server,avatar,  userinfo,poll,  status,temp,    define")
    embed.add_field(name = "Actions", value = "hug,kick,punch,pat,  stab,kidnap,slap,rr", inline=True)
    embed.add_field(name = "Valorant", value = "loadout, agent,(agnet)_info", inline=True)
    embed.add_field(name = "Math", value = "add,sub,div,    multi,rando,(3D shape),trigno")
    embed.add_field(name = "Reactions", value = "yes,no")
    embed.add_field(name = "Greetings", value = "gm,ga,gn,gd")
    embed.add_field(name = "Physics", value = "reflection,      refraction,      ref_index")
    embed.add_field(name = "General", value = "timer,reminder,report,dm,dm_all,snipe")

    embed.add_field(name = "Syntax", value = "For tell and hi syntx is .hi (message), for .tell\n.td is for truth or dare\nFor all the action commands you have to mention member\nFor all math commands syntax is '.add 2 5'\nFor the greeting commands you have to mention user\nFor timer you have to specify how many seconds\nFor reminder you have to specify how many seconds and message to remind\nFor report syntax is .report @mention (reason)\nFor dm and dm_all syntax is .dm @mention (message), .dm_all (message)", inline=False)

    await ctx.send(embed=embed)

client.run('ODI4NDk2ODg1NjQ3OTMzNDcx.YGqb2g.SFYkLd47BgUvUATVSaNyYZq7lzw')
