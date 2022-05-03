import discord
import os
import requests
import json


dtoken = 'OTcwMzQyODA2NzY3OTM5NjA2.Ym6kKQ.vLPy8NFmWD9UAdiUZ7pjxMqyylo'

commandInfo = """$pkid- gets the id of the specified pokemon \n$pkability - sends the pokemon standard ability\n$pkhability - sends hidden ability of pokemon
\n $pksprite - sends a picture of the sprite"""

def getPkInfo(pokemon):
    pk = requests.get('https://pokeapi.co/api/v2/pokemon/' + pokemon)
    x = pk.json()
    return x

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    
    msg = message.content

    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if msg.startswith('$pkid'):
        pkmn = msg.split()
        y = getPkInfo(pkmn[1])
        await message.channel.send(y['id'])
    
    if msg.startswith('$pkability'):
        pkmn = msg.split()
        y = getPkInfo(pkmn[1])
        await message.channel.send(y["abilities"][0]['ability']['name'])
    
    if msg.startswith('$pkhability'):
        pkmn = msg.split()
        y = getPkInfo(pkmn[1])
        await message.channel.send(y["abilities"][1]['ability']['name'])
    
    if msg.startswith('$pksprite'):
        pkmn = msg.split()
        y = getPkInfo(pkmn[1])
        await message.channel.send(y['sprites']['front_default'])
    
    if msg.startswith('$help'):
        await message.channel.send(commandInfo)

        

client.run(dtoken)