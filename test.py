from unicodedata import name
from urllib import request
from urllib.request import urlopen
import requests
import json

def getPkInfo(pokemon):
    pk = requests.get('https://pokeapi.co/api/v2/pokemon/' + pokemon)
    x = pk.json()
    print(x["abilities"][0]['ability']['name'])

getPkInfo('ditto')