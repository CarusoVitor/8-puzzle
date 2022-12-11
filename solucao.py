from _collections import deque

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

    # caminho é a lista de movimentos dos nós anteriores
    def pegaRaiz(self, caminho=[]):
        # Insere a si mesmo
        caminho.insert(0, self.acao)
        # Se tem pai, pede que ele busque a raiz
        if self.pai is not None:
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
    X = []
    F = deque([Nodo(estado, None, None, 0)])
    while len(F) != 0:
        v = F.popleft()  # Pega primeiro elemento
        if v.estado == "12345678_":
            return v.pegaRaiz()

        if v not in X:
            X.append(v)  # Insere no fim da lista (fila)
            vizinhos = expande(v)
            for vizinho in vizinhos:
                F.append(vizinho)
    return -1


if __name__ == "__main__":
    nodos = bfs("123_45678")
    for nodo in nodos:
        print(nodo)

