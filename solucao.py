class Nodo:
    def __init__(self, acao: str, estado: str, pai, custo: int):
        self.acao = acao
        self.estado = estado
        self.pai = pai
        self.custo = custo

    def __str__(self):
        return f"acao:{self.acao}, estado:{self.estado}, pai:{repr(self.pai)}, custo:{self.custo}"

    def __repr__(self):
        return f"Nodo({self.acao}, {self.estado}, {self.pai}, {self.custo})"


def sucessor(estado: str):
    index_branco : int = estado.find('_')
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
    conjunto_nodos = [Nodo(movimento[0], movimento[1], nodo, nodo.custo+1) for movimento in movimentos]
    return conjunto_nodos

if __name__ == "__main__":
    nodo_pai = Nodo("null", "2_3541687", None, 0)
    nodos = expande(nodo_pai)
    for nodo in nodos:
        print(nodo)

