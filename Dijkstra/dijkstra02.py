DISTANCE = 0
ANTERIOR = 1
INFINITY = float("inf")

map = {
    "A": {"B": 4, "C": 3},
    "B": {"A": 4, "C": 5, "D": 2},
    "C": {"A": 3, "B": 5, "D": 1, "E": 3},
    "D": {"B": 2, "C": 1, "E": 4},
    "E": {"C": 3, "D": 4}
}

tabela = {
    "A": [0, None],
    "B": [INFINITY, None],
    "C": [INFINITY, None],
    "D": [INFINITY, None],
    "E": [INFINITY, None]
}

def pega_menor_distancia(tabela, vertice):
    return tabela[vertice][DISTANCE]

def seta_menor_distancia(tabela, vertice, distance):
    tabela[vertice][DISTANCE] = distance

def seta_anterior(tabela, vertice, anterior):
    tabela[vertice][ANTERIOR] = anterior

def pega_distancia(map, primeiro_vertice, segundo_vertice):
    return map[primeiro_vertice][segundo_vertice]

def pega_proximo_vertice(tabela, visitado):
    nao_visitados = list(
        set(tabela.keys()).difference(visitado)
    )

    vertice_minimo = nao_visitados[0]
    distancia_minima = tabela[nao_visitados[0]][DISTANCE]

    for vertice in nao_visitados:
        if tabela[vertice][DISTANCE] < distancia_minima:
            vertice_minimo = vertice
            distancia_minima = tabela[vertice][DISTANCE]
   
    return vertice_minimo

def encontra_menor_caminho(map, tabela, origem):
    visitado = []
    atual = origem
    inicio = origem

    while True:
        vertice_adjacente = map[atual]

        if set(vertice_adjacente).issubset(visitado):
            pass
        else:
            nao_visitados = set(vertice_adjacente).difference(set(visitado))

            for vertice in nao_visitados:
                distancia_do_comeco = pega_menor_distancia(tabela, vertice)

                if distancia_do_comeco == INFINITY and inicio == atual:
                    distancia_total = pega_distancia(map, atual, vertice)
                else:
                    distancia_total = pega_menor_distancia(tabela, atual)
                    distancia_total += pega_distancia(map, atual, vertice)
               
                if distancia_total < distancia_do_comeco:
                    seta_menor_distancia(tabela, vertice, distancia_total)
                    seta_anterior(tabela, vertice, atual)
               
        visitado.append(atual)

        if len(visitado) == len(tabela.keys()):
            break
       
        atual = pega_proximo_vertice(tabela, visitado)

    return tabela

resultado = encontra_menor_caminho(map, tabela, "A")
print(resultado)