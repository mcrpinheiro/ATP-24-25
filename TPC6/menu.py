from tpc6 import *

def menu():
    turma = []
    opcao = input('''Bem vindo! O que deseja fazer?
                (1) Criar uma turma;
                (2) Inserir um aluno na turma;
                (3) Listar a turma;
                (4) Consultar um aluno por id;
                (8) Guardar a turma em ficheiro;
                (9) Carregar uma turma dum ficheiro;
                (0) Sair da aplicação''')
    novaopcao = ('''O que deseja fazer agora?
                (1) Criar uma turma;
                (2) Inserir um aluno na turma;
                (3) Listar a turma;
                (4) Consultar um aluno por id;
                (8) Guardar a turma em ficheiro;
                (9) Carregar uma turma dum ficheiro;
                (0) Sair da aplicação''')
    while opcao != '0':
        if opcao in ['2', '3', '4', '5', '6', '7', '8'] and turma == []:
            opcao= input('''Ainda não existe uma turma. Deseja criar ou carregar uma turma?
                  (1) Criar uma turma
                  ...
                  (9) Carregar uma turma dum ficheiro
                  (0) Sair''')
        if opcao == '1':
            nralunos= int(input('Quantos alunos terá a turma?'))
            turma = criarTurma (nralunos)
            print(turma)
            opcao = input(novaopcao)
        elif opcao == '2':
            turma = inserirAluno(turma)
            opcao = input(novaopcao)
        elif opcao == '3':
            print(listarTurma(turma))
            opcao = input(novaopcao)
        elif opcao == '4':
            idConsulta = int(input('Qual id deseja consultar?'))
            print(consultarID(turma, idConsulta))
            opcao = input(novaopcao)
        elif opcao == '8':
            nomefile = input('Qual o nome do ficheiro onde deseja guardar a turma?')
            guardarTurma(turma, nomefile)
            opcao = input(novaopcao)
        elif opcao =='9':
            nomefile = input('Qual o nome do ficheiro de onde deseja carregar a turma?')
            turma = carregarTurma(nomefile)
            print('A turma foi carregada com sucesso!')
            opcao = input(novaopcao)
    print('Obrigado e volte sempre!')

menu()