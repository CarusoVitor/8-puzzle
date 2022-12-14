from collections import deque
from time import time
import heapq

class Nodo:
    def __init__(self, estado: str or None, pai, acao: str or None, custo: int):
        self.acao = acao
        self.estado = estado
        self.pai = pai
        self.custo = custo

    def __str__(self):
        return f"acao:{self.acao}, estado:{self.estado}, pai:{repr(self.pai)}, custo:{self.custo}"

    def __repr__(self):
        return f"Nodo({self.acao}, {self.estado})"

    def __eq__(self, other):
        return self.estado == other.estado

    def __hash__(self):
        return hash(self.estado)

    def __lt__(self, other):
        return self.custo < other.custo

    # caminho é a lista de movimentos dos nós anteriores
    def pegaRaiz(self, caminho = None):
        if caminho is None:
            caminho = []
        # Se tem pai, pede que ele busque a raiz
        if self.pai is not None:
            caminho.insert(0, self.acao) # Insere a si mesmo
            return self.pai.pegaRaiz(caminho)
        return caminho


def sucessor(estado: str):
    index_branco: int = estado.find('_')
    estado = list(estado)
    movimentos = []

    # movimento direita
    if index_branco % 3 != 2:
        index_direita = index_branco + 1
        estado_direita = estado.copy()
        estado_direita[index_branco], estado_direita[index_direita] = estado_direita[index_direita], estado_direita[index_branco]
        movimentos.append(("direita", ''.join(estado_direita)))

    # movimento esquerda
    if index_branco % 3 != 0:
        index_esquerda = index_branco - 1
        estado_esquerda = estado.copy()
        estado_esquerda[index_branco], estado_esquerda[index_esquerda] = estado_esquerda[index_esquerda], estado_esquerda[index_branco]
        movimentos.append(("esquerda", ''.join(estado_esquerda)))

    # movimento cima
    index_cima = index_branco - 3
    if index_cima >= 0:
        estado_cima = estado.copy()
        estado_cima[index_branco], estado_cima[index_cima] = estado_cima[index_cima], estado_cima[index_branco]
        movimentos.append(("acima", ''.join(estado_cima)))

    # movimento baixo
    index_baixo = index_branco + 3
    if index_baixo <= 8:
        estado_baixo = estado.copy()
        estado_baixo[index_branco], estado_baixo[index_baixo] = estado_baixo[index_baixo], estado_baixo[index_branco]
        movimentos.append(("abaixo", ''.join(estado_baixo)))

    return movimentos


def expande(nodo):
    movimentos = sucessor(nodo.estado)
    conjunto_nodos = [Nodo(estado, nodo, acao, nodo.custo + 1) for acao, estado in movimentos]
    return conjunto_nodos


def bfs(estado):
    X = set()
    F = deque([Nodo(estado, None, None, 0)])
    while len(F) != 0:
        v = F.popleft()  # Pega primeiro elemento
        if v.estado == "12345678_":
            print(len(X))
            return v.pegaRaiz()
        if v not in X:
            X.add(v)
            vizinhos = expande(v)
            for vizinho in vizinhos:
                F.append(vizinho) # Insere no fim da lista (fila)
    return None


def dfs(estado, profundidade_maxima=65):
    profundidade_atual = 0
    while profundidade_atual < profundidade_maxima:
        X = set()
        F = deque([Nodo(estado, None, None, 0)])
        while len(F) != 0:
            v = F.pop()  # Pega ultimo elemento
            if v.estado == "12345678_":
                print(len(X))
                return v.pegaRaiz()
            if v not in X and v.custo < profundidade_atual:
                X.add(v)
                vizinhos = expande(v)
                for vizinho in vizinhos:
                    F.append(vizinho) # Insere no fim da pilha
        profundidade_atual += 1
    return None


def heuristica_hamming(estado):
    pecas_fora_lugar = 0
    for p in range(len(estado)-1):
        if str(p+1) != estado[p]:
            pecas_fora_lugar += 1
    return pecas_fora_lugar


def heuristica_manhattan(estado):
    distancias_manhattan = 0
    for index in range(len(estado)):
        peca = estado[index]
        if peca != '_':
            linha_correta = (int(peca) - 1) // 3
            coluna_correta = (int(peca) - 1) % 3
            linha_atual = index // 3
            coluna_atual = index % 3
            distancia_vertical = abs(linha_correta - linha_atual)
            distancia_horizontal = abs(coluna_correta - coluna_atual)
            distancias_manhattan += distancia_vertical + distancia_horizontal
            
    return distancias_manhattan


def astar_hamming(estado):
    X = set()
    custo_inicial = 0
    # Insere no formato (f(item), item)
    F = [(heuristica_hamming(estado)+custo_inicial, Nodo(estado, None, None, custo_inicial))]
    while len(F) != 0:
        v = heapq.heappop(F)[1] # Pega elemento de menor custo
        if v.estado == "12345678_":
            print(len(X))
            return v.pegaRaiz()
        if v not in X:
            X.add(v)
            vizinhos = expande(v)
            for vizinho in vizinhos:
                heapq.heappush(F, (heuristica_hamming(estado)+vizinho.custo, vizinho)) # Insere na fila de prioridades
    return None


def astar_manhattan(estado):
    X = set()
    custo_inicial = 0
    # Insere no formato (f(item), item)
    F = [(heuristica_manhattan(estado)+custo_inicial, Nodo(estado, None, None, custo_inicial))]
    while len(F) != 0:
        v = heapq.heappop(F)[1] # Pega elemento de menor custo
        if v.estado == "12345678_":
            print(len(X))
            return v.pegaRaiz()
        if v not in X:
            X.add(v)
            vizinhos = expande(v)
            for vizinho in vizinhos:
                heapq.heappush(F, (heuristica_manhattan(estado)+vizinho.custo, vizinho)) # Insere na fila de prioridades
    return None


if __name__ == "__main__":
    print("########### BFS ###########")
    t1 = time()
    nodos1 = bfs("2_3541687")
    print(time() - t1)
    if nodos1 is not None:
        print(len(nodos1))
        for nodo in nodos1:
            print(nodo)
    else:
        print("Nao encontrou caminho")


    print("\n########### DFS ###########")
    t2 = time()
    nodos2 = dfs("2_3541687")
    print(time() - t2)    
    if nodos2 is not None:
        print(len(nodos2))
        for nodo in nodos2:
            print(nodo)
    else:
        print("Nao encontrou caminho")

    print("\n########### A* Hamming ###########")
    t3 = time()
    nodos3 = astar_hamming("2_3541687")
    print(time() - t3)    
    if nodos3 is not None:
        print(len(nodos3))
        for nodo in nodos3:
            print(nodo)
    else:
        print("Nao encontrou caminho")

    print("\n########### A* Manhattan ###########")
    t4 = time()
    nodos4 = astar_manhattan("2_3541687")
    print(time() - t4)
    if nodos4 is not None:
        print(len(nodos4))
        for nodo in nodos4:
            print(nodo)
    else:
        print("Nao encontrou caminho")
