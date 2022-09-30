from discord.ext import commands
from bot_token import tok
import aiocron
from googlesearch import search
from bs4 import BeautifulSoup
import requests

def randomWord():
    word_generator = requests.get( \
        'https://www.coolgenerator.com/5-letter-word-generator' \
).text.encode("utf-8")
    soup = BeautifulSoup(word_generator, 'lxml')
    word_box = soup.find('li', class_='col-sm-4 col-xs-6')
    word = word_box.find('p', class_='text-center font-18')
    return str(word.find('span'))[6:11]


#client = discord.Client()
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@aiocron.crontab('00 00 * * *')
async def daily_wordle():
    WURMPLE_CHANNEL=bot.get_channel(967143913615929435)
    toGuess = str(randomWord().lower())
    await WURMPLE_CHANNEL.send('https://cdn.discordapp.com/attachments/ \
967143913615929435/967153996613709824/unknown.png')
    await WURMPLE_CHANNEL.send('OMG babe! New wordle just dropped! \
        *Sloppy mouth to mouth combat noises*'
        + '\nhttps://www.nytimes.com/games/wordle/index.html' + \
            '\nGive ' + toGuess + " a try.") 



@bot.command()
async def test(ctx, arg1):
    await ctx.send(arg1)

@bot.command()
async def goog(ctx, query):
    async with ctx.typing():
        for j in search(query, tld="co.in", num=1, stop=1, pause=2):
            await ctx.send(f"{j}")


@bot.event
async def on_message(message):
    split_message_lower = message.content.lower().split(' ')

    if message.author == bot.user:
        return
    if ("im" in split_message_lower):
        await message.channel.send("hi " + ''.join([split_message_lower[i] + \
' ' for i in range(split_message_lower.index("im") + 1, \
    len(split_message_lower))]) + "im dad")
    if ("i'm" in split_message_lower):
        await message.channel.send("hi " + ''.join([split_message_lower[i] + \
' ' for i in range(split_message_lower.index("i'm") + 1, \
    len(split_message_lower))]) + "im dad")

    await bot.process_commands(message)

#py -3 gs_bot.py
bot.run(tok, bot=True)
