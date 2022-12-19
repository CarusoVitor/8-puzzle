# 8-puzzle

INF01048 - Inteligência Artificial - 2022/2

Léo Hernandes de Vasconcelos - 323961<br>
Jose Henrique Lima Marques - 324502<br>
Vítor Caruso Rodrigues Ferrer - 327023


## Resultados obtidos

Executamos os algoritmos com a entrada "2_3541687" e analisamos quantos nós são expandidos, o tempo decorrido e qual o custo da solução encontrada.


| Algoritmos | Nodos expandidos | Tempo de execução (em seg) | Custo do caminho |
|------------|------------------|----------------------------|------------------|
| BFS | 22 | 0.698350191116333 | 23 |
| DFS | 32 | 2.649228096008301 | 33 |
| A* (heurística hamming) | 22 | 2.6974940299987793 | 23 | 
| A* (heurística manhattan) | 22 | 3.0969581604003906 | 23 |
