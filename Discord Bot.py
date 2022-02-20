#Encourage bot
# https://discord.com/api/oauth2/authorize?client_id=944647394878947358&permissions=257088&scope=bot

import os
import discord
from pip._vendor import requests
import json
import random
from compliments import resp_comp
import time

X_API_KEY = 'e2124031-8b25-41af-99b1-7949b78e088a'

client = discord.Client()

goodNight = ['night', 'goodnight', 'night!', 'sleep well', 'Sleep', 'SLEEP']
salutations = ['Good Night', 'Sleep Well', 'Sleep Tight', 'Go Get Some Rest', 'See You Tomorrow']

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' -'+ json_data[0]['a']
    return quote

def get_cat_fact():
    response = requests.get('https://catfact.ninja/fact')
    json_data = json.loads(response.text)
    fact = json_data['fact']
    return fact

def get_activity():
    response = requests.get('https://www.boredapi.com/api/activity')
    json_data = json.loads(response.text)
    activity = json_data['activity']
    return activity


def get_apod():
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=JAwLHYyMbW01Pbke0dsfzv6VJ8Jygt1Au9PenYeV')
    json_data = json.loads(response.text)
    apod = json_data['url']
    return apod

def get_dog_pic():
    response = requests.get('https://dog.ceo/api/breeds/image/random?api_key=e2124031-8b25-41af-99b1-7949b78e088a')
    json_data = json.loads(response.text)
    dog = json_data['message']
    return dog

def get_cat_pic():
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    json_data = json.loads(response.text)
    cat = json_data[0]['url']
    return cat

def get_joke():
    response = requests.get('https://v2.jokeapi.dev/joke/any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=twopart')
    json_data = json.loads(response.text)
    joke = json_data['setup']+'\n'+json_data['delivery']
    return joke


def get_compliment():
    compliment = random.choice(resp_comp)
    return compliment


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    msg = message.content
    if message.author == client.user:
        return

    elif message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    elif message.content.startswith('$help'):
        embedVar = discord.Embed(title="Help Page", description="Here is a list of all the things you can ask me to do!", color=0xffd3b6)
        embedVar.add_field(name="$help", value="I'll send you a list of all the commands you can ask me.", inline=False)
        embedVar.add_field(name="$inspire", value="I'll send you an inspirational quote.", inline=False)
        embedVar.add_field(name='$compliment', value="I'll send you a compliment", inline=False)
        embedVar.add_field(name="$catfact", value="I will send you a random cat fact.", inline=False)
        embedVar.add_field(name="$dogpic", value="I'll send a picture of a dog.", inline=False)
        embedVar.add_field(name="$catpic", value="I'll send you a picture of a cat.", inline=False)
        embedVar.add_field(name='$apod', value="I'll send you the NASA Astronomy Picture of the Day", inline=False)
        embedVar.add_field(name="$joke", value="I'll send you a joke.", inline=False)
        embedVar.add_field(name="$activity", value="I'll send you an activity to do.", inline=False)
        await message.channel.send(embed=embedVar)
        

    elif message.content.startswith('$compliment'):
        compliment = get_compliment()
        await message.channel.send(compliment)

    elif message.content.startswith('$catfact'):
        fact = get_cat_fact()
        await message.channel.send(fact) 

    
    elif message.content.startswith('$activity'):
        activity = get_activity()
        await message.channel.send(activity)
    

    elif message.content.startswith('$dogpic'):
        dog = get_dog_pic()
        await message.channel.send(dog)

    elif message.content.startswith('$catpic'):
        cat = get_cat_pic()
        await message.channel.send(cat)

    elif message.content.startswith('$apod'):
        apod = get_apod()
        embedVar = discord.Embed(title="Nasa Astronomy Picture of the Day", description="Here is the Astronomy Picture of the Day (APOD) from\nhttps://www.nasa.gov/", color=0xffd3b6)
        embedVar.set_image(url=apod)
        await message.channel.send(embed=embedVar)

    elif message.content.startswith('$joke'):
        joke = get_joke()
        await message.channel.send(joke)

    elif any(word in msg for word in goodNight):
        await message.channel.send(random.choice(salutations))
  

client.run(os.getenv('TOKEN'))