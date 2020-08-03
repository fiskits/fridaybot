# created by u/The_Meme-Connoisseur

import discord
from discord.ext import commands, tasks
from discord import Client
import datetime
import asyncio

bot = commands.Bot(command_prefix = '!')

friday = 4
send_time = '14:00'
# replace channel_id with your channel's ID
channel_id = 000000000000000000
# replace token with your bot's token
token = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
filename = 'birthdays.csv'


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
        birthday_list = open(filename,'r')
        # checks birthday list for any birthdays
        for entry in birthday_list:
            string = birthday_list.readline()
            info = string.split(',')
            name = info[0]
            birth_day = int(info[1])
            birth_month = int(info[2])
            birth_year = int(info[3])
            # sends message
            if (day == birth_day and month == birth_month):
                age = year - birth_year
                wish_string = 'Happy ' + str(age) + determine_ordinal(age) + ' birthday, ' + name + '!\nhttps://imgur.com/a/G3wEPyg'
                await channel.send(wish_string)
        birthday_list.close()



@bot.event
async def on_member_join(member):
    await bot.wait_until_ready()
    channel = bot.get_channel(channel_id)
    await channel.send(f'Hello {member.name}! I\'m Garfield. If you want me to wish you a happy birthday, just type \'!birthday [preferred name] [day of birthday] [month of birthday] [year of birthday]\'')

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
    if message.author == bot.user:
        return
    if lasaga in text:
        await message.channel.send('*lasaga')
    if garfield in text:
        await message.channel.send(f'I eat, {message.author.name}. It\'s what I do')
    if where_are_the in text or wheres_the in text:
        await message.channel.send('I eat those food')
    if i_hate in text:
        await message.channel.send('I hate alram clocks')
    if bad_bot in text:
        await message.channel.send('sowwy uwu')
    if crabs in text:
        await message.channel.send('🦀🦀🦀 crab rave 🦀🦀🦀')
    if good_bot in text:
        await message.channel.send('Thanks! *brup*')
    await bot.process_commands(message)


@bot.command(pass_context=True)
async def birthday(ctx,*args):
    channel = bot.get_channel(channel_id)
    # prevents bot from responding to itself
    if (ctx.author == bot.user):
        return
    # ensures right number of arguments
    if (len(args) != 4):
        await channel.send('Oops! I didn\'t get that. Please try again using this format:\n!birthday Garfield 19 6 1978')
        return
    # puts content of *args in a list
    string = '{} '.format(' '.join(args))
    arg_list = string.split()
    # checks formatting
    if ((not arg_list[1].isnumeric()) or (not arg_list[2].isnumeric()) or (not arg_list[3].isnumeric())):
        await channel.send('It looks like you formatted it wrong. Please put your name, day, month, and year like this:\n!birthday Garfield 19 6 1978')
        return
    # converts elements of list to proper types
    name = arg_list[0]
    day = int(arg_list[1])
    month = int(arg_list[2])
    year = int(arg_list[3])
    # ensures the date is valid
    if (day < 0 or day > 31 or month < 0 or month > 12):
        await channel.send('Oops! You may have mixed up the day and month. Put the day first, like this:\n!birthday Garfield 19 6 1978')    
        return
    # stores info
    birthday_list = open(filename,'a')
    info = name + ',' + str(day) + ',' + str(month) + ',' + str(year) + '\n'
    birthday_list.write(info)
    birthday_list.close()
    # sends confirmation
    await channel.send(f'Ok {name}, I\'ll wish you a happy birthday on ' + get_month(month) + ' ' + str(day) + determine_ordinal(day))
    


def determine_ordinal(x):
    # determines what to put after a number to make it an ordinal
    if (x % 10 == 1 and x % 100 != 11):
        return 'st'
    elif (x % 10 == 2 and x % 100 != 12):
        return 'nd'
    elif (x % 10 == 3 and x % 100 != 13):
        return 'rd'
    else:
        return 'th'

def get_month(month):
    month_list = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return month_list.get(month, "Invalid month")

bot.run(token)
