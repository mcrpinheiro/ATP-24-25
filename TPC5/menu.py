from tpc5 import *

def menu():
    cinema = []
    opcao = input('''Bem vindo, o que deseja fazer?
    (1) Criar um cinema
    (2) Inserir cinema
    (3) Listar filmes
    (4) Confirmar disponibilidade de lugar
    (5) Vender um bilhete
    (6) Listar disponibilidade 
    (7) Inserir uma nova sala
    (8) Ver o cinema 
    (0) Sair\n''')
    novaopcao= ('''O que deseja fazer agora?
    (1) Criar um cinema
    (2) Inserir cinema
    (3) Listar filmes
    (4) Confirmar disponibilidade de lugar
    (5) Vender um bilhete
    (6) Listar disponibilidade 
    (7) Inserir uma nova sala
    (8) Ver o cinema 
    (0) Sair\n''')
 
    while opcao != '0':
        if opcao in ['3', '4', '5', '6', '7', '8'] and cinema == []:
            opcao = input ('''Ainda não existe um cinema. O que deseja fazer agora?
                           (1) Criar um cinema
                           (0) Sair''')
        if opcao == '1':
            cinema = criarCinema()
            print(f'O cinema criado é: {verCinema(cinema)}')
            opcao = input(novaopcao)
        elif opcao == '2':
            salas = int(input('Quantas salas terá o cinema?'))
            i = 1
            while salas > 0:
                nrlugares = int(input(f'Quantos lugares terá a sala {i}?'))
                filme = input(f'Qual será o filme exibido na sala {i}?')
                novasala = [nrlugares, [], filme]
                cinema = inserirSala(cinema, novasala)
                i = i + 1
                salas = salas - 1
            opcao = input(novaopcao)
        elif opcao == '3':
            print(f'{listar(cinema)}')
            opcao = input(novaopcao)
        elif opcao == '4':
            ver = input('Para qual filme deseja verificar a disponibilidade?')
            lugar = input('Qual lugar quer confirmar se está disponível?')
            if disponivel(cinema, ver, lugar) == True: print('Este lugar encontra-se disponível.')
            else: print('Lamentamos, este lugar encontra-se indisponível.')
            opcao = input(novaopcao)
        elif opcao == '5':
            fil = input('Para qual filme deseja comprar um bilhete?')
            bil = input('Qual o lugar do bilhete que deseja comprar?')
            if disponivel(cinema, fil, bil) == 'disponivel':
                print(f'O bilhete para {fil} no lugar {bil} foi vendido com sucesso.')
                cinema = vendebilhete(cinema,fil, bil)
                opcao = input(novaopcao)
            else:
                print('Lamentamos, este lugar encontra-se indisponível.')
                opcao = input(novaopcao)
        elif opcao == '6':
            print(listardisponibilidades(cinema))
            opcao = input(novaopcao)
        elif opcao == '7':
            nrlugares = int(input('Quantos lugares terá a nova sala?'))
            filme = input('Qual será o filme exibido nesta sala?')
            novasala = [nrlugares, [], filme]
            inserirSala(cinema, novasala)
            print('Esta sala foi adicionada com sucesso ao cinema.')
            opcao = input(novaopcao)
        elif opcao == '8':
            print(verCinema(cinema))
            opcao = input(novaopcao)
    print('Obrigado e volte sempre!')
menu()
