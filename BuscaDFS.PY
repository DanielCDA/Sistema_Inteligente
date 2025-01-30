# Definindo o grafo como um dicionário de listas de adjacência
grafo = {
    'A': ['B'],
    'B': ['A', 'C', 'D', 'E'],
    'C': ['B', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D', 'F', 'G'],
    'F': ['E', 'H'],
    'G': ['E', 'H'],
    'H': ['F', 'G']
}

def dfs(grafo, inicio, objetivo):
    pilha = [(inicio, [inicio])]
    visitados = set()

    while pilha:
        no, caminho = pilha.pop()
        if no == objetivo:
            return caminho
        if no not in visitados:
            visitados.add(no)
            for vizinho in reversed(grafo[no]):  # Revertendo para manter a ordem correta
                pilha.append((vizinho, caminho + [vizinho]))

    return None

# Executando a DFS
caminho = dfs(grafo, 'H', 'A')
print("Caminho encontrado:", caminho)