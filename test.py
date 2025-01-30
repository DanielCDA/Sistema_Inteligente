from collections import deque

# Definindo o grafo como um dicionário de listas de adjacência
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F', 'G'],
    'F': ['C', 'E', 'H'],
    'G': ['E'],
    'H': ['F']
}

def bfs(grafo, inicio, objetivo):
    fila = deque([(inicio, [inicio])])
    visitados = set()

    while fila:
        no, caminho = fila.popleft()
        if no == objetivo:
            return caminho
        if no not in visitados:
            visitados.add(no)
            for vizinho in grafo[no]:
                fila.append((vizinho, caminho + [vizinho]))

    return None

# Executando a BFS
caminho = bfs(grafo, 'A', 'C')
print("Caminho ótimo:", caminho)