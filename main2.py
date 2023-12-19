# 導入Discord.py模組
import discord
# 導入commands指令模組
from discord.ext import commands
from snownlp import SnowNLP
import jieba as ja
from GGG import gg
from yt import ytv
import yt_dlp
from firebase import firebase
import json
    
with open("Token.json",'r') as f:
    data = json.load(f)
url = data['url']
fdb = firebase.FirebaseApplication(url, None)
TOKEN = data['token']


# intents是要求機器人的權限
intents = discord.Intents.all()
import random
# command_prefix是前綴符號，可以自由選擇($, #, &...)
bot = commands.Bot(command_prefix = "!", intents = intents,case_insensitive=True)

@bot.event
# 當機器人完成啟動
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel")
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

@bot.command(name='play', help='To play song')
async def play(ctx, url):
    ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': '%(title)s.%(etx)s',
            'quiet': False
        }
    song_info = yt_dlp.YoutubeDL(ydl_opts).extract_info(url, download=False)
    voice_client = ctx.message.guild.voice_client
    if not voice_client.is_connected():
        await ctx.send("Bot is not connected to a voice channel.")
        return
    voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=song_info['url']))
    
    
@bot.command(name='pause', help='Pause the song')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        voice_client.pause()
        await ctx.send("Music paused")
    else:
        await ctx.send("No music is playing right now.")
        
@bot.command(name='resume', help='Resume the song')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        voice_client.resume()
        await ctx.send("Music resumed")
    else:
        await ctx.send("Music is not paused.")
        
@bot.command(name='hello', help='say hello')
# 輸入!Hello呼叫指令
async def Hello(ctx):
    # 回覆Hello, world!
    await ctx.send("Hello, world!")
    
    
@bot.command(name='fat', help='say fat')
# 輸入!fat呼叫指令
async def fat(ctx):
    # 回覆Hello, world!
    await ctx.send("You are fat!")

@bot.command()
# 輸入!fat呼叫指令
async def dice(ctx):
    # 回覆Hello, world!
    await ctx.send(random.randrange(1,7,1))

@bot.command()
# 輸入!parrot 文字呼叫指令
async def parrot(ctx,message):
    analysis_list = list(ja.cut(message))
    if len(analysis_list)>1:
        await ctx.send(analysis_list[len(analysis_list)-2]+analysis_list[len(analysis_list)-1])
    else:
        await ctx.send(message)
    
@bot.command()
# 輸入!emotion 文字呼叫指令
async def emotion(ctx,message):
    s = SnowNLP(message)
    if s.sentiments>0.51:
        await ctx.send('O')
    else:
        await ctx.send('X')

@bot.command()
# 輸入!yt 文字呼叫指令
async def yt(ctx,message):
    consequence=ytv(message)
    await ctx.send(consequence)
    
@bot.command()
# 輸入!ytc 文字呼叫指令
async def ytc(ctx,message):
    if message=="1":
        v = fdb.get('/','v1')
        await ctx.send(v)
        fdb.put('/','x','')
    elif message=="2":
        v = fdb.get('/','v2')
        await ctx.send(v)
        fdb.put('/','x','')
    elif message=="3":
        v = fdb.get('/','v3')
        await ctx.send(v)
        fdb.put('/','x','')
    else:
        await ctx.send("選擇1或2或3")

@bot.command()
# 輸入!emotion 文字呼叫指令
async def goo(ctx,message):
    consequence=gg(message)
    await ctx.send(consequence)
    
    
bot.run(TOKEN)