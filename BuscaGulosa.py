from queue import PriorityQueue

# Definição do grafo
grafo = {
    'A': {'B': 10},
    'B': {'C': 8, 'D': 5, 'E': 20},
    'C': {'E': 9},
    'D': {'E': 15},
    'E': {'F': 8, 'G': 6},
    'F': {'H': 4},
    'G': {'H': 5},
    'H': {}
}

# Heurísticas
heuristica = {
    'A': 23,
    'B': 34,
    'C': 12,
    'D': 13,
    'E': 5,
    'F': 8,
    'G': 9,
    'H': 0
}

# Função para busca gulosa
def busca_gulosa(grafo, inicio, objetivo, heuristica):
    visitados = set()
    fila = PriorityQueue()
    fila.put((heuristica[inicio], inicio, [inicio]))
    
    while not fila.empty():
        (h, no, caminho) = fila.get()
        if no == objetivo:
            return caminho
        if no not in visitados:
            visitados.add(no)
            for vizinho, custo in grafo[no].items():
                if vizinho not in visitados:
                    fila.put((heuristica[vizinho], vizinho, caminho + [vizinho]))
    return None


# Execução dos algoritmos
inicio = 'A'
objetivo = 'H'

caminho_guloso = busca_gulosa(grafo, inicio, objetivo, heuristica)


print("Caminho encontrado pela busca gulosa:", caminho_guloso)
