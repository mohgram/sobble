import discord
import asyncio
import random
import time
import logging
from discord import Client
from discord.ext import commands
bot = commands.Bot(command_prefix=commands.when_mentioned_or('drip!'))
bot.remove_command('help')
@bot.event
async def on_ready():
    print('bot is up')
    activity = discord.Activity(name='quarentine|drip!help', type=discord.ActivityType.playing)
    await bot.change_presence(activity=activity)
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Here's your help help!", description="This is the help command help page!")
    embed.add_field(name="fhelp_[pagenumber]", value="The main aspect of the bot, fun!", inline=False)
    embed.add_field(name="mhelp", value="The 2nd aspect of the bot, moderation!", inline=False)
    embed.add_field(name="dhelp", value="Help for DBL commands!", inline=False)
    embed.add_field(name="faq", value="Frequently Asked Questions", inline=False)
    await ctx.send(embed=embed)
@bot.command()
async def suggest(ctx):
          emoji = '\N{THUMBS UP SIGN}'
          aemoji = '\N{THUMBS DOWN SIGN}'
          query = ctx.message.content
          stopwords = ['sb!suggest']
          querywords = query.split()
          resultwords = [word for word in querywords if word.lower() not in stopwords]
          info= ' '.join(resultwords)     
          embed = discord.Embed(title="Suggestion!", description=info, colour=0x00ff00)
          embed.add_field(name="Suggester", value=ctx.author, inline=False)
          channel = bot.get_channel(646075728642834443)
          await channel.send(embed=embed)
          await ctx.message.add_reaction(emoji)
          await ctx.messageObject.add_reaction(emoji)
          await ctx.messageObject.add_reaction(aemoji) 
@bot.command()
async def fhelp_1(ctx):
        embed = discord.Embed(title="Here's your fun help!", description="Page 1 of 3", color=0x206694)
        embed.add_field(name="fhelp", value="Help is brought up", inline=False)
        embed.add_field(name="suggest [suggestion]", value="Suggests an idea to be added to SobbleBot", inline=False)
        embed.add_field(name="calmingmusic", value="Gives you a video of calming waves.", inline=False)
        embed.add_field(name="dab", value="?????", inline=False)
        embed.add_field(name="story", value="tells you a nice little story with you as the main character!", inline=False)
        await ctx.send(embed=embed)
@bot.command() 
async def fhelp_2(ctx):
        embed = discord.Embed(title="Here's your fun help!", description="Page 2 of 3")            
        embed.add_field(name="wisdom", value="Random wisdom.", inline=False)
        embed.add_field(name="eightball", value="An 8ball function that sees the future.", inline=False)
        embed.add_field(name="dice",value="Guess a number of 6, if the computer sees the same, you win!", inline=False)
        embed.add_field(name='coinflip', value="It flips a coin.", inline=False)
        embed.add_field(name="joke", value="Tells you a funny joke.", inline=False)
        await ctx.send(embed=embed)
@bot.command()
async def fhelp_3(ctx):
        embed = discord.Embed(title="Here's your help!", description="This is page 3 of Fun Help!For page one, do drip!fhelp!")        
        embed.add_field(name="highfive", value="High five!", inline=False)
        embed.add_field(name="vanish", value="Provides a vanishing GIF.", inline=False)
        embed.add_field(name="dance", value="Provides a dancing GIF", inline=False)
        embed.add_field(name="randmeme", value="Gives you a meme out of an ever growing list", inline=False)
        embed.add_field(name="drift", value="kansei dorifto!", inline=False)
        await ctx.send(embed=embed)
@bot.event()
async def on_guild_join():
    embed = discord.Embed(title="Thanks for adding me!", description="My name is SobbleBot, Agent SobbleBot. ")    
    embed.add_field(name="Operation Join Server is accomplished.", description="https://cdn.discordapp.com/attachments/336642776609456130/648509688480268308/5025d60f9100f844d6294c3d6c2e32c8-1.png")   
    await ctx.send(embed=embed)     
@bot.command()
async def mhelp(ctx, arg):
    embed = discord.Embed(title="Here's your moderation help!", description="Moderation help is here!")
    embed.add_field(name="sbban", value="Bans a user", inline=False)
    embed.add_field(name="sbunban", value="Unbans a user", inline=False)
    embed.add_field(name="sbmute", value="Mutes a user[creates a role called muted]", inline=False)
    embed.add_field(name="sbunmute", value="Unmutes a user", inline=False)
    await ctx.send(embed=embed)
@bot.command()
async def faq(ctx):
    embed = discord.Embed(title="Here's your SobbleBot FAQ!", description="Frequently asked questions")
    embed.add_field(name="Who made this bot?", value="Devble#3618 did!", inline=False)
    embed.add_field(name="What's the support server?", value="https://discord.gg/8uQ4EeX", inline=False)
    await ctx.send(embed=embed)
@bot.command()
async def calmingmusic(ctx):
    await ctx.send("***https://www.youtube.com/watch?v=j5a0jTc9S10***")
@bot.command()
async def wisdom(ctx):
    wisdom = ["You can't get banned from a server if you follow the rules.","A sort of life is better than no life.","Some servers aren't worth going to.","Don't obsess over everything."]
    wisdomc = random.choice(wisdom)
    await ctx.send(wisdomc)
@bot.command()
async def eightball(ctx): 
        messag = ["Yes.", "It is certain", "Probably", "50/50", "There is a low probability.", "No."]
        message = random.choice(messag)
        await ctx.send(message)

@bot.command()
async def dice(ctx):
        botdice =["sbdice 1","sbdice 2","sbdice 3","sbdice 4","sbdice 5","sbdice 6"]
        botdi = random.choice(botdice)
        if ctx.message.content == botdi:
            await ctx.send("You were right! :partying_face: ")
        else:
            await ctx.send("you were wrong. :pensive:")
@bot.command()
async def joke(ctx):
        await ctx.send("Why did the chicken cross the road? It was getting to the idiot's house.")
        time.sleep(5)
        await ctx.send("Knock knock.")
        time.sleep(3)
        await ctx.send("It's the chicken.")
@bot.command()
async def facts(ctx):
    await ctx.send("https://imgur.com/a/H63R8hG")
@bot.command()
async def coinflip(ctx):
        coin = ["Heads", "Tails"]
        coinf = random.choice(coin)
        await ctx.send(coinf)
@bot.command()
async def story(ctx):
        await ctx.send("I see you would like a story. Now preparing...")
        await ctx.send (f"You are {ctx.message.author}, correct?")
        if 'yes' or 'YES' in message.content:
         await ctx.send (f"Okay then, {ctx.message.author} The great legend of {ctx.message.author} is about to begin!")
         embed = discord.Embed(name=f"The story of {ctx.message.author}", description="By DripBot")
         embed.add_field("Don't like the story? Add a suggestion!")
         await ctx.send(f"{ctx.message.author} was going on a stroll,
@bot.event    
async def on_message(message):
 if message.author == bot.user:
      return
 if message.content.startswith('<@645009678224457740>'):    
     await message.channel.send("Use drip!help to find all the commands!")
 await bot.process_commands(message)

@bot.command()
async def joined(ctx, member: discord.Member):
    embed = discord.Embed(name="When did they join?", description="Hmm, when did they join?")
    embed.add_field(name="Let's see... oh I know!", value="{0.name} joined in {0.joined_at}!".format(member))
    embed.add_field(name="The time system", value="It's YYYY-MM-DD")
    await ctx.send(embed=embed)   
@bot.command()
async def dance(ctx):
    await ctx.send("https://tenor.com/view/dancing-coffin-coffin-dance-funeral-funny-farewell-gif-16737844")
@bot.command()
async def dab(ctx):
    await ctx.send("You asked.")
    time.sleep(1)
    await ctx.send("https://cdn.discordapp.com/attachments/385837258768515083/645685851698888704/165ouZ0gVczfHuvwCma1S96R7I0wAAAABJRU5ErkJggg.png")
@bot.command()
async def randmeme(ctx):
        meme = ["https://cdn.discordapp.com/attachments/645695800352964618/646018286504509440/ae6f07ce-085e-11ea-8da7-95ed4a38ab68.png","https://cdn.discordapp.com/attachments/645695800352964618/646018152743829514/EU-internet-meme_trans_NvBQzQNjv4BqpJliwavx4coWFCaEkEsb3pVDAZXwknrCGX2X3jMDFdw.png","https://cdn.discordapp.com/attachments/645695800352964618/646018080878624788/label-face-crowd-text-homedecor-person-human.png","https://cdn.discordapp.com/attachments/645695800352964618/646017964226904094/e0uhelxpmkm31.png", "https://i.redd.it/rwfpxonc0nz31.jpg", "https://preview.redd.it/vr89p4mf5nz31.jpg?width=640&crop=smart&auto=webp&s=98f4ec3d7e5a4c7b80c8178b5a714883cab795ad", "https://preview.redd.it/lbaosswd2oz31.jpg?width=640&crop=smart&auto=webp&s=7c5e4b6f2dcbadc7c48b0fe0078b327b40a95745", "https://preview.redd.it/bizn2l9qanz31.jpg?width=640&crop=smart&auto=webp&s=cc68cf8eb224ee6a58495e96be074b1ad844ea04", "https://preview.redd.it/bhf5et6y6oz31.jpg?width=640&crop=smart&auto=webp&s=8c03dd198478a09d1627afad3d47084153962eeb", "https://preview.redd.it/tmdhramd0nz31.jpg?width=640&crop=smart&auto=webp&s=52a4c5b04a115a478b9441d2b0a8b27cc33575c9", "https://preview.redd.it/66b0rfktlmz31.jpg?width=640&crop=smart&auto=webp&s=9893a79032204593c1177435117c8ea27ff70dcd", "https://preview.redd.it/jn7060kmwnz31.jpg?width=640&crop=smart&auto=webp&s=e66d4ccbd3b2985af35d94397ea8b1b7287e0369", "https://preview.redd.it/4j0bknoj4nz31.jpg?width=640&crop=smart&auto=webp&s=ce9de25e30f3bbdbfe2e73f2827e00ded833a055", "https://preview.redd.it/kax0nm6ycnz31.jpg?width=640&crop=smart&auto=webp&s=002c64f8d8d98dfdba74c58188abaa697fb9581d", "https://preview.redd.it/lckm8ryw9nz31.jpg?width=640&crop=smart&auto=webp&s=3a3e55fb01bd8e376a5023a1487dd105b29308b7", "https://preview.redd.it/s786dtyhsnz31.jpg?width=640&crop=smart&auto=webp&s=cf22f41f0aac182a98288abc5ce2a27fb87ece67", "https://preview.redd.it/frai7o57knz31.jpg?width=640&crop=smart&auto=webp&s=aa669a7ce9d75bf1f7799d88a3cc2fa8de19b35f", "https://preview.redd.it/qn5uczwbcnz31.jpg?width=640&crop=smart&auto=webp&s=fb0b9c3cee2280b37ac703bf54819cf05d064839", "https://i.redd.it/xbs7mcla8oz31.png", "https://external-preview.redd.it/56hO7MTgDT4zxmAxycINZ319yWXbfbpc6uBkmYQ12Aw.jpg?width=640&crop=smart&auto=webp&s=d07e4004c7f35b485ffaab67f93270adfa5dab11", "https://preview.redd.it/47xuwt4vcmz31.jpg?width=640&crop=smart&auto=webp&s=426d95aeb070dc6ece565301a0b22cb74696a5e8"]
        memes = random.choice(meme)
        await ctx.send(memes)
@bot.command()
async def drift(ctx):
        await ctx.send("...k..kansei dorifto!?!?")
        await ctx.send("https://gfycat.com/zigzagbasicblackpanther")


#Moderation
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
           await ctx.send("There's no right for you to be using this command!(Missing Permissions)")
                


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, * , reason=None):
  if member is None:
      await ctx.send("Please input an actual person!")
  else:         
   await member.kick(reason=reason)
   await ctx.send("GAME! That user's been kicked.")  
@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, member : discord.Member, * , reason=None): 
  if member is None:    
      await ctx.send("There's no user to unban!")
  else:      
   await member.unban(reason=reason)
   await ctx.send("*door opens* That user has been unbanned")
@bot.command() 
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, * , reason=None): 
  if member is None:    
      await ctx.send("There's no user to ban!")
  else:      
   await member.ban(reason=reason)
   await ctx.send("*door shuts* That user has been banned")
@bot.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx, member : discord.Member = None, mutetime: typing.Optional[int] = 0,*, reason="None"):
     role = discord.utils.get(ctx.guild.roles, name="Muted")

     if member == None:
        await ctx.send('Please pass in a valid user')
        return
     await member.add_roles(role)
     await ctx.channel.send(f'{member} was muted!')
     if mute_time > 0:
      await asyncio.sleep(mutetime)
      await member.remove_roles("Muted", reason)
@bot.command()
async def jojoke():
     await ctx.send("You expected a jojoke, but it was me, DIO!")
     await ctx.send("https://cdn.discordapp.com/attachments/559455534965850142/648223929613418526/Z.png")
     time.sleep(2)
     await ctx.send("shit that's a jojoke")
@bot.command()
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member : discord.Member = None):
    if member is None:
        await ctx.send('Please pass in a valid user')
        return
    else:
     await member.remove_roles("Muted")
     await ctx.send(f'{str(member)} was unmuted!')
bot.run('JOJO')
