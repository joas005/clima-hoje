import os
import time
import requests
import favorites
from unidecode import unidecode

def clearTerminal():
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')

def requestingAPI(city):
    API_KEY = 'ad66cd24346dd9eb3d79144fc041f047'
    link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=pt_br"
    try:
        req = requests.get(link)
        requisicao_dic = req.json()
        description = requisicao_dic['weather'][0]['description']
        temp = requisicao_dic['main']['temp'] - 273.15
        countryOrigin = requisicao_dic['sys']['country']
        return description, temp, countryOrigin
    except: 
        print('\033[31m\nVocê inseriu uma cidade inválida!\033[0m\nTente novamente.')
        clearTerminal()

def choosingCity():
    while True:
        city = input(
            '\nVocê deseja ver o clima de qual cidade? ').strip().lower()
        if requestingAPI(unidecode(city)):
            description, temp, countryOrigin = requestingAPI(unidecode(city))
            return city.title(), description, temp, countryOrigin

def printingCity(city, description, temp, countryOrigin, favorite):
    print(f'\nAtualmente em \033[35m- {city}, {countryOrigin} -\033[0m o clima está: ')
    print(f'\033[1;34mCéu: {description}\n\033[35mTemperatura: {round(temp, 1)} °C\033[0m\n')
    if not favorite:
        input('\nEnter continua...')
        addFavorite = input('Deseja adicionar esta cidade a sua lista de favoritos? ').strip().lower()
        if addFavorite in ['sim', 'si', 's', 'y', 'yes']:
            if city not in favorites.favoriteCitysList:
                favorites.addToFavortites(city)
            else:
                print('Esta cidade já está na sua lista de favoritos!')
                clearTerminal()