# TPC 4: Aplicação para manipulação de listas de inteiros
### Autor: Maria Pinheiro

O TPC 4 consiste na realização de uma aplicação para manipulação de listas de inteiros. Este foi dividido em 2 ficheiros:
* *menu.py* - onde se encontra a aplicação principal;
* *tpc4.py*  - onde estão as funções para correr o jogo.

### Funções da Aplicação
Nesta aplicação (em *menu.py*), é possível escolher entre várias opções para analisar uma lista de inteiros, se esta já estiver criada. Caso esta não esteja criada, a aplicação obriga o utilizador a criar um lista aleatória ou com números escolhidos pelo próprio.
Considerando isto, cada opção do menu tem a sua função respetiva (em *tpc4.py*), que irá realizar a operação desejada.
* (1) Criar Lista: `criaLista()` - recebe um número inteiro introduzido pelo utilizador, e cria uma lista com esse tamanho;
* (2) Ler Lista: `introduzLista()` - recebe um número inteiro introduzido pelo utilizador, e cria uma lista com números escolhidos pelo mesmo com o tamanho escolhido;
* (3) Soma: `somaLista(lista)` - recebe uma lista e calcula a soma dos elementos dessa lista;
* (4) Média: `mediaLista(lista)` - recebe uma lista e calcula a média dos elementos dessa lista;
* (5) Maior: `maiorLista(lista)` - recebe uma lista e calcula o maior valor dessa lista;
* (6) Menor: `menorLista(lista)` - recebe uma lista e calcula o menor valor dessa lista;
* (7) estaOrdenada por ordem crescente: `estaOrdenadaC(lista)` - recebe uma lista e verifica se esta está ordenada de forma crescente, devolvendo `True` se estiver ordenada e `False` caso contrário; 
* (8) estaOrdenada por ordem decrescente: `estaOrdenadaD(lista)` - recebe uma lista e verifica se esta está ordenada de forma decrescente, devolvendo `True` se estiver ordenada e `False` caso contrário; 
* (9) Procura um elemento: `procuraEl(lista, elemento)` - recebe uma lista e um inteiro e devolve o indíce onde esse elemento se encontra na lista; caso este não exista, devolve -1.


