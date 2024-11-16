
def criarTurma (nralunos):
    turma = []
    i = 1
    while i <= nralunos:
        print(f'Informações do Aluno {i}:')
        turma = inserirAluno(turma)
        i = i + 1
    return turma

def inserirAluno (turma):
    nome = input(f'Qual o nome do aluno?')
    id = input(f'Qual o id do aluno?')
    notaTPC = int(input(f'Qual a nota dos TPCs do aluno?'))
    notaProj = int(input(f'Qual a nota do Projeto do aluno?'))
    notaTeste = int(input(f'Qual a nota do teste do aluno?'))
    aluno = (nome,id, [notaTPC, notaProj, notaTeste]) 
    if aluno not in turma:
        turma.append(aluno)
    else:
        print('Este aluno já existe!')
    return turma

def listarTurma (turma):
    for aluno in turma:
        print(aluno)
    return turma

def consultarID (turma, id):
    alunoID = ''
    for aluno in turma:
        if aluno[1] == id:
            alunoID = aluno
    return alunoID

def linha (aluno):
    res = str(aluno[0]) + '::' + str(aluno[1]) + '::' + str(aluno[2][0])+ '::' + str(aluno[2][1])+ '::' + str(aluno[2][2]) + '\n'
    return res

def guardarTurma (turma, ficheiro):
    file = open(ficheiro, "w")
    for alunos in turma:
        file.write(linha(alunos))
    file.close()

def carregarTurma (ficheiro):
    turma = []
    file = open(ficheiro, "r")
    for linha in file:
        listaLinha = linha.split('::')
        aluno = (listaLinha[0], int(listaLinha[1]),[int(listaLinha[2]), int(listaLinha[3]), int(listaLinha[4].split('\n')[0])])
        turma.append(aluno)
    return turma

