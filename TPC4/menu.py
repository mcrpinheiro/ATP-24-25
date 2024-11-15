from tpc4 import *

def menu():
    lista = []
    opcao = input('''Bem vindo à aplicação de manipulação de inteiros. O que deseja fazer?
        (1) Criar Lista 
        (2) Ler Lista
        (3) Soma
        (4) Média
        (5) Maior
        (6) Menor
        (7) estaOrdenada por ordem crescente
        (8) estaOrdenada por ordem decrescente
        (9) Procura um elemento
        (0) Sair
            ''')
    novomenu = '''O que deseja fazer agora?
        (1) Criar Lista 
        (2) Ler Lista
        (3) Soma
        (4) Média
        (5) Maior
        (6) Menor
        (7) estaOrdenada por ordem crescente
        (8) estaOrdenada por ordem decrescente
        (9) Procura um elemento
        (0) Sair'''
    while opcao != '0':
        if opcao in ['3','4','5','6','7','8','9'] and lista==[]:
            opcao = input('''Não se esqueça de criar uma lista. O que deseja fazer?
            (1) Criar Lista 
            (2) Ler Lista
            (0) Sair''')

        if opcao == '1':
            lista = criaLista()
            print(f'A lista resultante foi {lista}.')
            opcao = input(novomenu)
        elif opcao == '2':
            lista = introduzLista()
            print(f'A lista resultante foi {lista}.')
            opcao = input(novomenu)
        elif opcao == '3':
            print(f'A soma dos elementos da lista é {somaLista(lista)}.')
            opcao = input(novomenu)
        elif opcao == '4':
            print(f'A média de todos os elementos da lista é {mediaLista(lista)}.')
            opcao = input(novomenu)
        elif opcao == '5':
            print(f'O maior número da lista é {maiorLista(lista)}.')
            opcao = input(novomenu)
        elif opcao == '6':
            print(f'O menor número da lista é {menorLista(lista)}.')
            opcao = input(novomenu)
        elif opcao == '7':
            if estaOrdenadaC(lista) == True: print('Sim.')
            else: print('Não.')
            opcao = input(novomenu)
        elif opcao == '8':
            if estaOrdenadaD(lista) == True: print('Sim.')
            else: print('Não.')
            opcao = input(novomenu)
        elif opcao == '9':
            elemento = int(input('Escolha um elemnto para procurar na lista:'))
            print(f'O elemento está no índice {procuraEl(lista, elemento)}.')
            opcao = input(novomenu)
    print(f' A lista final foi {lista}. Obrigado e volte sempre!')
        
menu()