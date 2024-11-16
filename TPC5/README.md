# TPC 5: Aplicação para Gerir um Cinema
### Autor: Maria Pinheiro

O TPC 5 consiste na realização de uma aplicação para gerir um conjutno de salas de cinema de um centro comercial. Este foi dividido em 2 ficheiros:
* *menu.py* - onde se encontra a aplicação principal;
* *tpc5.py*  - onde estão as funções para correr o jogo.


### Funções da Aplicação
Para a realização deste exercício, consideramos que um cinema é uma lista de salas. Por sua vez, salas são uma lista com 3 elementos - o número de lugares total na sala (um inteiro), uma lista com os lugares cujos bilhetes já foram vendidos (lista de inteiros) e o nome do filme exibido nessa sala (uma string).

Nesta aplicação (em *menu.py*), é possível escolher entre várias opções para gerir um cinema, se esta já estiver criado. Caso esta não esteja criado, a aplicação obriga o utilizador a criar um cinema aleatório ou a inserir um cinema.
Considerando isto, cada opção do menu tem a sua função respetiva (em *tpc5.py*), que irá realizar a operação desejada.
* (1) Criar um cinema: `criarCinema()`- a função cria um cinema aleatório, com algumas limitações, isto é, o número de salas é limitado entre 1 e 10, o número de lugares entre 10 e 50, e o filme é escolhido através de uma lista com filmes aleatórios;
* (2) Inserir cinema: na opção inserir cinema, o utilizador escolhe um número de salas e para cada uma das salas escolhe o número de lugares total e o filme exibido na mesma;
* (3) Listar filmes: `listar(cinema)` - a função recebe um cinema e lista todos os filmes exibidos no mesmo no momento;
* (4) Confirmar disponibilidade de lugar: `disponivel(cinema, filme, lugar)` - a função recebe um cinema, um filme, e um lugar e confirma se esse lugar está disponível para esse filme, devolvendo True no caso do lugar estar disponível, e False no caso contrário.
* (5) Vender um bilhete: `vendebilhete(cinema, filme, lugar)` - a função recebe um cinema, um filme, e um lugar, e adiciona o lugar escolhido à lista de lugares vendidos na sala onde o filme está a ser exibido, devolvendo o cinema com esta lista atualizada.
* (6) Listar disponibilidade: `listardisponibilidades(cinema)` - a função recebe um cinema e lista quantos lugares estão disponíveis em cada sala do mesmo.
* (7) Inserir uma nova sala: `inserirSala(cinema, sala)` - a função recebe um cinema e uma sala, e adiciona a sala especificada ao cinema, devolvendo o cinema atualizado.
* (8) Ver o cinema: `vercinema(cinema)` - a função recebe um cinema, e devolve uma string constituida por todas as informações de cada sala



