from queue import PriorityQueue

# Definição do grafo
grafo = {
    'A': {'B': 10},
    'B': {'C': 8, 'D': 15, 'E': 20},
    'C': {'E': 9},
    'D': {'H': 4},
    'E': {'F': 6, 'G': 5},
    'F': {'H': 5},
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

# Função para busca A*
def busca_a_estrela(grafo, inicio, objetivo, heuristica):
    visitados = set()
    fila = PriorityQueue()
    fila.put((heuristica[inicio], 0, inicio, [inicio]))
    
    while not fila.empty():
        (f, g, no, caminho) = fila.get()
        if no == objetivo:
            return caminho, g
        if no not in visitados:
            visitados.add(no)
            for vizinho, custo in grafo[no].items():
                if vizinho not in visitados:
                    novo_g = g + custo
                    novo_f = novo_g + heuristica[vizinho]
                    fila.put((novo_f, novo_g, vizinho, caminho + [vizinho]))
    return None, float('inf')

# Função para busca competitiva
def busca_competitiva(grafo, inicio, objetivo, heuristica):
    # Executa a busca gulosa
    caminho_guloso = busca_gulosa(grafo, inicio, objetivo, heuristica)
    
    # Executa a busca A*
    caminho_a_estrela, custo_a_estrela = busca_a_estrela(grafo, inicio, objetivo, heuristica)
    
    # Calcula o custo do caminho encontrado pela busca gulosa
    custo_guloso = 0
    if caminho_guloso:
        for i in range(len(caminho_guloso) - 1):
            custo_guloso += grafo[caminho_guloso[i]][caminho_guloso[i+1]]
    
    # Compara os custos e seleciona o melhor caminho
    if caminho_guloso and caminho_a_estrela:
        if custo_guloso < custo_a_estrela:
            return caminho_guloso, custo_guloso
        else:
            return caminho_a_estrela, custo_a_estrela
    elif caminho_guloso:
        return caminho_guloso, custo_guloso
    elif caminho_a_estrela:
        return caminho_a_estrela, custo_a_estrela
    else:
        return None, float('inf')

# Execução do algoritmo de busca competitiva
inicio = 'A'
objetivo = 'H'

melhor_caminho, melhor_custo = busca_competitiva(grafo, inicio, objetivo, heuristica)

print("Melhor caminho encontrado:", melhor_caminho)
print("Custo do melhor caminho:", melhor_custo)