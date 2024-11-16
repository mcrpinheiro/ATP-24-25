# TPC 5: Aplicação para Gerir um Cinema
### Autor: Maria Pinheiro

O TPC 7 consiste na realização de uma aplicação para analisar uma tabela metereológica. Este foi dividido em 2 ficheiros:
* *menu.py* - onde se encontra a aplicação principal;
* *tpc7.py*  - onde estão as funções para correr o jogo.

Além disto, ainda existem 5 ficheiros auxiliares:
* `metereologia.txt` - ficheiro onde tem uma tabela metereológica guardada;
* `graficotempMax.png` - ficheiro resultante da criação de um gráfico das temperaturas máximas da tabela metereológica em `metereologia.txt`;
* `graficotempMin.png` - ficheiro resultante da criação de um gráfico das temperaturas mínimas da tabela metereológica em `metereologia.txt`;
* `graficochuva.png` - ficheiro resultante da criação de um gráfico das pluviosidade da tabela metereológica em `metereologia.txt`;
* `graficosjuntos.png` - combinação de todos os gráficos acima mencionados num só.

### Funções da Aplicação
Para a realização deste exercício, consideramos que uma tabela metereológica é uma lista de tuplos. Cada tuplo é respetivo a uma data (cuja é o primeito elemento do tuplo e um tuplo de 3 inteiros). Cada tuplo tem mais 3 elementos, floats, que correspondem à temperatura mínima, à temperatura máxima e à precipitação na data respetiva.

Nesta aplicação (em *menu.py*), é possível escolher entre várias opções para analisar uma tabela meterológica. Caso ainda não exista, o utilizador deve carregar um ficheiro de uma tabela metereológica, cujo formato deve ser, por linha:
ano::mês::dia::temperatura minima::temperatura maxima::precipitação
Como podemos ver no ficheiro *metereologia.txt*.

Considerando isto, cada opção do menu tem a sua função respetiva (em *tpc7.py*), que irá realizar a operação desejada.
* (1) Carregar uma tabela meteorológica de um ficheiro: `carregaTabMeteo(fnome)` - recebe um ficheiro `txt` com uma tabela metereológica e carrega a mesma para código;
* (2) Calcular a temperatura média de cada dia: `medias(tabMeteo)` - recebe uma tabela meterológica e devolve uma lista de tuplos, onde o primeiro elemento é uma data e o segundo a média das temperaturas nessa mesma data;
* (3) Calcular a temperatura mínima: `minTemp(tabMeteo)` - recebe uma tabela meterológica e devolve a temperatura mínima mai baixa;
* (4) Calcular a amplitude térmica de cada dia: `amplTerm(tabMeteo)` - recebe uma tabela meterológica e devolve uma lista de tuplos, onde o primeiro elemento é uma data e o segundo amplitude térmica nessa mesma data;
* (5) Calcular a precipitação máxima: `maxChuva(tabMeteo)` - recebe uma tabela meterológica e devolve um tuplo, onde o primeiro elemento é a data com maior precipitação e o segundo elemento o valor da precipitação nesse dataa;
* (6) Calcular o número de dias com precipitação superior a determinado valor: `diasChuvosos(tabMeteo, p)` - recebe uma tabela meterológica e um valor de precipitação `p` e devolve uma lista de tuplos, onde o primeiro elemento é uma data cuja precipitação foi superior ao valor `p` e o segundo a valor da precipitação nesse mesmo dia;
* (7) Calcular o maior número de dias consecutivos com precipitação inferior a determinado valor: `maxPeriodoCalor(tabMeteo, p)` - recebe uma tabela metereológica e um valor de precipitação `p` e devolve um inteiro que corresponde ao maior número de dias consecutivos com precipitação superior a `p`
* (8) Guardar uma tabela meteorológica num ficheiro:  `guardaTabMeteo(t, fnome)` - recebe uma tabela metereológica e um nome de um ficheiro, e guarda a tabela metereológica no mesmo com formato igual a `meterologia.txt`.
* (9) Criar um gráfico com a tabela meteorológica: `grafTabMeteo(tabMeteo, tipo)` - recebe uma tabela meterológica e uma variável `tipo` do tipo string e devolve um gráfico. A variável tipo é inserida pelo utilizador, e consuante esta, o gráfico final vai varir:
    * (A) [Gráfico das temperaturas mínimas](./graficochuva.png) - cria um gráfico com todas as temperaturas mínimas da tabela meterológica;
    * (B) [Gráfico das temperaturas máximas](./graficotempMax.png) - cria um gráfico com todas as temperaturas máximas da tabela meterológica;
    * (C) [Gráfico da pluvisioidade](./graficochuva.png) - cria um gráfico com todos os valores de precipitação da tabela meterológica ;
    * (D) [Gráfico de todas as variáveis juntas](./graficosjuntos.png) - cria um gráfico com os 3 gráficos acima.

