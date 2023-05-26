import request
import favorites
import os
os.system('cls' if os.name == 'nt' else 'clear')

menu = ['Ver clima por busca', 'Ver lista de favoritos', 'Créditos', 'Sair']

favorites.createFavorites()

def showCredits():
    print('\n\033[34mObrigado por querer me conhecer\033[0m 😁✌️\nEste programa foi desenvolvido por \033[35m@joas005\033[0m no github, entre lá para conheça um pouco mais sobre mim e meus projetos!')
    input('\nEnter continua...')

def exitingProgram():
    print('\033[32m\nObrigado por utilizar meu programa!\033[0m\nVolte sempre que precisar planejar seu look perfeito do dia 😁')
    favorites.saveFavorites()
    exit()

print("\033[35mComo está o clima hoje?\033[0m\n")

print('\033[32mBem-vindo!\033[0m\n\nOlá! Você está usando o app \033[35mClima Hoje!\033[0m Um aplicativo desenvolvido para você dar uma olhadinha em como está o clima agora de qualquer cidade do mundo!\n')

while True:
    print('O que você deseja fazer?\n')
    for n, item in enumerate(menu):
        print(f'[{n + 1}] {item}.')
    mode = input('>> ').strip().capitalize()

    if mode in menu:
        mode = str(menu.index(mode) + 1)

    match (mode):
        case '1':
            city, description, temp,countryOrigin = request.choosingCity() 
            request.printingCity(city, description, temp, countryOrigin, False)   
        case '2': favorites.seeFavorites()
        case '3': showCredits()
        case '4': exitingProgram()
        case _: 
            print('\033[31mVocê inseriu algo inválido!\033[0m\n Tente novamente.')
    request.clearTerminal()
