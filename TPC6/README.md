# TPC 6: Aplicação para Gerir uma Turma
### Autor: Maria Pinheiro

O TPC 6 consiste na realização de uma aplicação para gerir uma turma de alunos. Este foi dividido em 2 ficheiros:
* *menu.py* - onde se encontra a aplicação principal;
* *tpc6.py*  - onde estão as funções para correr a aplicação.
Além disto, ainda existe um ficheiro resultante da [criação de uma turma com 5 alunos](#criação-de-turma-de-5-alunos):
* `turmas.txt`.

### Funções da Aplicação
Para a realização deste exercício, consideramos que uma turma é uma lista de anos. Por sua vez, um aluno corresponde a um tuplo com 3 - o nome do aluno (sting), o id (inteiro) e uma lista de 3 inteiros que correspondem à nota do projeto, nota dos TPCs e nota do teste.

Nesta aplicação (em *menu.py*), é possível escolher entre várias opções para gerir a turma, se esta já estiver criada. Caso esta não esteja criada, a aplicação faz com que o utilizador crie uma turma, inserindo as informações individuais do aluno, ou carregue uma turma de um ficheiro texto. 

Considerando isto, cada opção do menu tem a sua função respetiva (em *tpc6.py*), que irá realizar a operação desejada.
* (1) Criar uma turma: `criarTurma(nralunos)` - recebe um inteiro que corresponde ao número de alunos, e cria uma turma com informações dadas pelo utilizador para cada aluno; 
* (2) Inserir um aluno na turma: `inserirAluno(turma)` - recebe uma turma, pede ao utilizador a informação do aluno, e adiciona o mesmo à turma, devolvendo a turma atualizada;
* (3) Listar a turma: `listarAlunos(turma)` - recebe uma turma e lista todos os alunos nessa turma;
* (4) Consultar um aluno por id: `consultarID(turma, id)` - recebe uma turma e um ID e devolve o aluno correspondente a esse ID;
* (8) Guardar a turma em ficheiro: `guardarTurma (turma, ficheiro)` - recebe uma turma e um nome de um ficheiro, e guarda essa turma no ficheiro, sendo cada linha do ficheiro correspondente a um aluno, com o formato: `Nome::ID::NotaTPC::NotaProj::NotaTeste`;
* (9) Carregar uma turma dum ficheiro: `carregarTurma (ficheiro)` - recebe um nome de um ficheiro, e carrega uma turma desse ficheiro, que deve estar com o mesmo formato acima mencionado.

### Criação de Turma de 5 Alunos
Para criar uma turma de 5 alunos, podemos recorrer à primeira opção do menu, escolhendo 5 como o número de alunos.
* O primeiro aluno será a Maria, com id 123, nota dos TPCS 10, nota do projeto 12, e nota do teste 11.
* O segundo aluno será o Joao, com id 456, nota dos TPCS 17, nota do projeto 12, e nota do teste 13.
* O terceiro aluno será a Ana, com id 67, nota dos TPCS 6, nota do projeto 9, e nota do teste 13.
* O quarto aluno será a Vanessa, com id 127, nota dos TPCS 3, nota do projeto 8, e nota do teste 10.
* O último aluno será a Joana, com id 140, nota dos TPCS 7, nota do projeto 5 e nota do teste 9.

A turma criada então, é:
```[('Maria', '123', [10, 12, 11]), 
('Joao', '456', [17, 12, 13]), 
('Ana', '67', [6, 9, 13]), 
('Vanessa', '127', [3, 8, 10]), 
('Joana', '140', [7, 5, 9])]
```
Utilizando a última opção para guardar esta turma num ficheiro, obtemos o ficheiro [turmas](./turmas.txt)



