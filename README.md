# 8-puzzle

INF01048 - Inteligência Artificial - 2022/2

Léo Hernandes de Vasconcelos - 323961<br>
Jose Henrique Lima Marques - 324502<br>
Vítor Caruso Rodrigues Ferrer - 327023


## Resultados obtidos

Executamos os algoritmos com a entrada "2_3541687" e analisamos quantos nós são expandidos, o tempo decorrido e qual o custo da solução encontrada.

| Algoritmos                | Nodos expandidos | Tempo de execução (em seg) | Custo do caminho |
|---------------------------|------------------|----------------------------|------------------|
| BFS                       | 109477           | 0.7802739143371582         | 23               |
| DFS                       | 64240            | 2.5529022216796875         | 33               |
| A* (heurística hamming)   | 107023           | 2.17108154296875           | 23               | 
| A* (heurística manhattan) | 107023           | 3.0002217292785645         | 23               |
