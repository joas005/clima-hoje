import os
import time
import request
from unidecode import unidecode

favoriteCitysList = []
menuFavorites = ['Remover cidade', 'Deletar lista', 'Editar lista', 'Sair']

def createFavorites():
    if os.path.isfile('favoritesCitys.txt'):
        with open('favoritesCitys.txt', 'r') as favoritesCitys:
            favoritesCitys.seek(0, os.SEEK_END)
            isempty = favoritesCitys.tell() == 0
            favoritesCitys.seek(0)
        if isempty == False:
            with open("favoritesCitys.txt", "r", encoding='utf=8') as data:
                for lines in data.readlines():
                    city, space = lines.split('\n')
                    if city not in favoriteCitysList:
                        favoriteCitysList.append(city)
                return favoriteCitysList
    else:
        return favoriteCitysList

def saveFavorites():
    with open('favoritesCitys.txt', 'w', encoding='utf=8') as favoritesCitys:
        for city in favoriteCitysList:
            favoritesCitys.write(city + '\n')

def editFavorites():
    request.clearTerminal() 
    print('\nVocê ecolheu editar sua lista!\n')
    while True:
        print('O que você deseja fazer?\n')
        for n, item in enumerate(menuFavorites):
            print(f'[{n + 1}] {item}.')
        mode = input('>> ').strip().capitalize()

        if mode in menuFavorites:
            mode = str(menuFavorites.index(mode) + 1)

        match(mode):
            case '1': removeCity()
            case '2': deleteList()
            case '3': editList()
            case '4': break
            case _:  print('\033[31mVocê inseriu algo inválido!\033[0m\n Tente novamente.')
        if not favoriteCitysList:
            break
        request.clearTerminal()

def removeCity():
    print('\033[31m\nVocê escolheu remover!\n\033[0m')
    for city in favoriteCitysList:
        print(f'{city}', end=' | ')
    removeItem = input(
        '\n\nQual cidade você deseja remover? ').strip().title()
    if removeItem in favoriteCitysList:
            removeFromFile(removeItem)
            favoriteCitysList.remove(removeItem)
            print(f'\033[31mCidade {removeItem} removida!\033[0m\n')
            for city in favoriteCitysList:
                print(f'{city}', end=' | ')
    else:  
        print('Cidade não encontrada!\nTente novamente.')

def removeFromFile(removeItem):
    removeLine = favoriteCitysList.index(removeItem) + 1
    with open("favoritesCitys.txt", "r") as favoritesCitys:
        lines = favoritesCitys.readlines()
        pointer = 1
        with open('favoritesCitys.txt', 'w') as favoritesCitys:
            for line in lines:
                if pointer != removeLine:
                    favoritesCitys.write(line)
                pointer += 1

def deleteList():
    confirm = input('\nTem certeza que deseja remover todos as cidades da sua lista? ').strip().lower()
    if confirm in ['sim', 'si', 's', 'y', 'yes']:
        print('Deletando sua lista de favoritos...')
        time.sleep(1.5)
        favoriteCitysList.clear()
        open('favoritesCitys.txt', 'w')
        print('Sua lista foi deletada.')
    else:
        print('\nUfa..\nEssa foi por pouco 😰')

def editList():
    print('\033[34m\nVocê escolheu editar!\n\033[0m')
    for city in favoriteCitysList:
        print(f'{city}', end=' | ')
    cityEdit = input(
        '\n\nQual das cidades acima você gostaria de editar? ') .strip().title()

    if cityEdit in favoriteCitysList:
        while True:
            newCity = input(
                f'Você gostaria de mudar \033[34m{cityEdit}\033[0m para o que? ') .strip().lower()
            if request.requestingAPI(unidecode(newCity)):
                for i in range(len(favoriteCitysList)):
                    if favoriteCitysList[i] == cityEdit:
                        favoriteCitysList[i] = newCity.title()  
                print(f'\n\033[31m{cityEdit}\033[0m alterado para \033[35m{newCity.title()}\033[0m.')
                editingFile(cityEdit, newCity.title())
                break
    else:
        print(f'\nCidade: {cityEdit} não encontrada em sua lista!\nTente novamente...')

def editingFile(cityEdit, newCity):
    with open('favoritesCitys.txt', 'r') as favoriteCitys:
        content = favoriteCitys.read()
    content = content.replace(cityEdit, newCity)
    with open('favoritesCitys.txt', 'w') as favoriteCitys:
        favoriteCitys.write(content)

def seeFavorites():
    if favoriteCitysList:
        for city in favoriteCitysList:
            description, temp, countryOrigin = request.requestingAPI(unidecode(city.lower()))
            request.printingCity(city, description, temp, countryOrigin, True)
        input('\nEnter continua...')
        edit = input('Você deseja alterar a sua lista de favoritos? ').strip().lower()
        if edit in ['sim', 'si', 's', 'y', 'yes']:
            editFavorites()
    else:
        print('\nSua lista de favoritos está vazia!\nTente adicionar algumas cidades para ver mais rapidamente os climas de cidades que são comuns para você!')
        input('\nEnter continua...')

def addToFavortites(city):
    print(f'\033[35mCidade {city}\033[0m adicionada aos seus favoritos!')
    favoriteCitysList.append(city)