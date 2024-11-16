from tpc7 import *

def menu():
    tabela = []
    opcao = input('''Bem vindo! O que deseja fazer?
                  (1) Carregar uma tabela meteorológica de um ficheiro
                  (2) Calcular a temperatura média de cada dia
                  (3) Calcular a temperatura mínima
                  (4) Calcular a amplitude térmica de cada dia
                  (5) Calcular a precipitação máxima
                  (6) Calcular o número de dis com precipitação superior a determinado valor
                  (7) Calcular o maior número de dias consecutivos com precipitação inferior a determinado valor
                  (8) Guardar uma tabela meteorólogica num ficheiro
                  (9) Criar um gráfico com a tabela meterológica
                  (0) Sair''')
    novaopcao = '''O que deseja fazer agora?
                  (1) Carregar uma tabela meteorológica de um ficheiro
                  (2) Calcular a temperatura média de cada dia
                  (3) Calcular a temperatura mínima
                  (4) Calcular a amplitude térmica de cada dia
                  (5) Calcular a precipitação máxima
                  (6) Calcular o número de dis com precipitação superior a determinado valor
                  (7) Calcular o maior número de dias consecutivos com precipitação inferior a determinado valor
                  (8) Guardar uma tabela meteorólogica num ficheiro
                  (9) Criar um gráfico com a tabela meterológica
                  (0) Sair'''
    while opcao != '0':
        if opcao in ['2', '3', '4', '5', '6', '7'] and tabela == []:
            print('''Não existe uma tabela metereológica em sistema! Deseja carregar uma?
                  (1) Carregar uma tabela meterológica de um ficheiro
                  (0) Sair''')
        if opcao == '1':
            file = input('Qual o nome do ficheiro que deseja carregar?')
            tabela = carregaTabMeteo(file)
            opcao = input(novaopcao)
        elif opcao == '2':
            print(medias(tabela))
            opcao = input(novaopcao)
        elif opcao == '3':
            print(minTemp(tabela))
            opcao = input(novaopcao)
        elif opcao == '4':
            print(amplTerm(tabela))
            opcao = input(novaopcao)
        elif opcao == '5':
            print(maxChuva(tabela))
            opcao =input(novaopcao)
        elif opcao == '6':
            minprec = float(input('Qual o valor mínimo de preciptação?'))
            print(diasChuvosos(tabela, minprec))
            opcao =input(novaopcao)
        elif opcao == '7':
            prec = float(input('Qual o valor máximo da precipitação?'))
            print(maxPeriodoCalor(tabela, prec))
            opcao =input(novaopcao)
        elif opcao == '8':
            t = [((2022,1,20), 2, 16, 0),((2022,1,21), 1, 13, 0.2), ((2022,1,22), 7, 17, 0.01)]
            guardaTabMeteo(t, 'metereologia.txt')
            opcao =input(novaopcao)
        elif opcao == '9':
            tipo = input('''Qual gráfico gostaria de ver?
                             (A) Gráfico das temperaturas mínimas
                             (B) Gráfico das temperaturas máximas
                             (C) Gráfico da pluvisioidade
                             (D) Gráfico de todas as variáveis juntas
                             (0) Sair''')
            if tipo not in ['A', 'B', 'C', 'D', '0']:
                tipo = input('''Opção indisponível, tente outra vez! Qual gráfico gostaria de ver?
                             (A) Gráfico das temperaturas mínimas
                             (B) Gráfico das temperaturas máximas
                             (C) Gráfico da pluvisioidade
                             (D) Gráfico de todas as variáveis juntas
                             (0) Sair''')
            grafTabMeteo(tabela, tipo)
            opcao = input(novaopcao)
    print('Obrigado e volte sempre!')

menu()