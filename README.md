# TeoriaDosGrafos
Teoria dos Grafos 2021.1  

- Avaliação I

Criar um sistema (software) para armazenar em memória um Grafo Simples (sem arestas paralelas ou laços) cuja definição seja inserida pelo usuário do sistema. Cada grupo fica livre para escolher a linguagem de programação(Python) e a plataforma do sistema(Opcional - Terminal ou interface). A forma como o usuário interage com o sistema para criar o grafo também fica livre para escolha de cada grupo. O sistema deverá ser capaz de criar grafos direcionados e não-direcionados (arestas com sentido ou não), valorados e não-valorados (arestas com pesos associados ou não). 

O usuário deverá ser capaz de interagir com o sistema para criar um grafo (2 pts).
O usuário poderá criar grafos direcionados e não-direcionados (0,5 pts). 
O usuário poderá criar grafos valorados e não-valorados (0,5 pts).
O usuário poderá ser capaz de imprimir o grafo (formato livre a ser definido pelo grupo, poder ser textual como uma lista de adjacência, matriz de adjacência, etc.) ou gráfico como imagem na tela ou download de arquivo de imagem (1 pt).
O usuário deverá conseguir obter a informação da Ordem do Grafo criado (0,5 pts).
O usuário deverá conseguir obter a informação do tamanho do grafo criado (0,5 pts).
Para um dado vértice o usuário deverá ser capaz de obter a informação da lista de vértices adjacentes. Se o grafo for direcionado, o sistema deverá ser capaz de informar a lista de vértices adjacentes de entrada e a lista de vértices adjacentes de saída do dado vértice (1 pt).
Para um dado vértice o sistema deverá ser capaz de informar o grau daquele vértice. Se o grafo for direcionado, o sistema deverá informar o grau de adjacência de entrada e de saída do vértice (0,5 pts).
Dado um par de vértices, o sistema deverá retornar a informação se os dois vértices são adjacentes ou não (0,5 pt).

- Avaliação II 

Utilizando o sistema implementado na Avaliação I, implementar uma funcionalidade que recebe um Grafo direcionado e valorado (arestas somente com pesos/custo positivos) como parâmetro de entrada e também um dos vértices do Grafo como outro parâmetro de entrada e calcula a menor distância entre este vértice e todos os outros do Grafo utilizando o algoritmo de Dijkstra. O sistema poderá também receber um segundo vértice como parâmetro, neste caso o resultado deverá ser o menor custo entre os dois vértices informados e também a sequência de vértices deste caminho de menor custo.
O usuário deverá ser capaz de inserir um Grafo e indicar 1 (um) vértice como origem. O sistema deverá informar o **menor custo** entre o vértice indicado e todos os outros vértices do Grafo (**2 pts**).
O usuário deverá ser capaz de inserir um Grafo e indicar 1 (um) vértice como origem. O sistema deverá informar a **sequência de vértices** de cada caminho de menor custo entre o vértice de origem e todos os outros vértices (**2,5 pts**).
O usuário deverá ser capaz de inserir um Grafo e indicar 2 (dois) vértices como origem e destino. O sistema deverá informar o **menor custo** entre os dois vértices indicados (**1 pt**).
O usuário deverá ser capaz de inserir um Grafo e indicar 2 (dois) vértices como origem e destino. O sistema deverá informar a **sequência de vértices** do caminho de menor custo entre estes dois vértices (**1,5 pts**).
