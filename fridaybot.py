# created by u/The_Meme-Connoisseur

import discord
from discord.ext import commands, tasks
from discord import Client
import datetime
import asyncio

bot = commands.Bot(command_prefix = '!')

friday = 4
send_time = '14:00' # set this to any time you want

# set channel_id to your channel's ID
channel_id = 000000000000000000
# set token to your bot's token
token = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
# set bot_id to your bot's ID
bot_id = 0000000000000000

class Member:
    # stores name and birthday of a member
    def __init__(self,name,day,month,year):
        self.name = name
        self.birth_day = day
        self.birth_month = month
        self.birth_year = year

# examples of members, please replace with your friends' info
weedman = Member('Weed Man',20,4,1980)
jesus = Member('Jesus',25,12,1)
member_list = [weedman,jesus]


@bot.event
async def on_ready():
    print('Friday again garfie baby')
    friday_again.start()
 
@tasks.loop(seconds=60)
async def friday_again():
    now = datetime.datetime.now()
    current_time = now.strftime('%H:%M')
    weekday = datetime.datetime.today().weekday()
    year = datetime.datetime.today().year
    month = datetime.datetime.today().month
    day = datetime.datetime.today().day
    channel = bot.get_channel(channel_id)
    if (str(current_time) == send_time):
        if (weekday == friday):
            # sends the Friday again garfie baby image on Fridays at 2:00 PM
            await channel.send('https://imgur.com/a/WrCgTLK')
        # wishes members a happy birthday
        for member in member_list:
            if (day == member.birth_day and month == member.birth_month):
                age = year - member.birth_year
                wish_string = 'Happy ' + str(age) + determine_ordinal(age) + ' birthday, ' + member.name + '!\nhttps://imgur.com/a/G3wEPyg'
                await channel.send(wish_string)



@bot.event
async def on_message(message):
    await bot.wait_until_ready()
    lasaga = 'lasagna'
    garfield = 'garfielf'
    where_are_the = 'where are the '
    wheres_the = 'where\'s the '
    i_hate = 'i hate '
    bad_bot = 'bad bot'
    good_bot = 'good bot'
    crabs = '🦀🦀🦀'
    text = message.content.strip().lower()
    # sends response if keyword(s) are in message
    if lasaga in text:
        await message.channel.send('*lasaga')
    if garfield in text:
        await message.channel.send(f'I eat, {message.author.name}. It\'s what I do')
    if where_are_the in text or wheres_the in text:
        await message.channel.send('I eat those food')
    if i_hate in text and message.author.id != bot_id:
        await message.channel.send('I hate alram clocks')
    if bad_bot in text:
        await message.channel.send('sowwy uwu')
    if crabs in text and message.author.id != bot_id:
        await message.channel.send('🦀🦀🦀 crab rave 🦀🦀🦀')
    if good_bot in text:
        await message.channel.send('Thanks! *brup*')

def determine_ordinal(age):
    # determines what to put after a number to make it an ordinal
    if (age % 10 == 1 and age % 100 != 11):
        return 'st'
    elif (age % 10 == 2 and age % 100 != 12):
        return 'nd'
    elif (age % 10 == 3 and age % 100 != 13):
        return 'rd'
    else:
        return 'th'

bot.run(token)