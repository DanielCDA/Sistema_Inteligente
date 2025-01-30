from collections import deque

def bfs(graph, start, goal):
    queue = deque([[start]])  # Fila inicial com o caminho contendo apenas o nó inicial
    visited = set([start])  # Conjunto para rastrear nós visitados, começando com o nó inicial
    
    while queue:
        path = queue.popleft()  # Obtém o primeiro caminho na fila
        node = path[-1]  # Último nó do caminho atual
        
        if node == goal:
            return path  # Retorna o caminho ótimo encontrado
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)  # Marca o nó como visitado
                new_path = path + [neighbor]  # Cria um novo caminho baseado no atual
                queue.append(new_path)  # Adiciona o novo caminho à fila
    
    return None  # Retorna None se não houver caminho

# Representação do grafo A como lista de adjacência
graph = {
    'A': ['B'],
    'B': ['A', 'C', 'D', 'E'],
    'C': ['B', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D', 'F', 'G'],
    'F': ['E', 'H'],
    'G': ['E', 'H'],
    'H': ['F', 'G']
}

# Definir o nó inicial e objetivo
start_node = 'A'
goal_node = 'H'

# Executar a busca BFS e imprimir o caminho
optimal_path = bfs(graph, start_node, goal_node)
print("Caminho ótimo encontrado:", optimal_path)
