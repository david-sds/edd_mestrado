import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Passo 1: Declaração de Variáveis e Entrada de Dados
N = 8  # Número de nós

# Arestas conforme sua definição
arestas = [
    (0, 1, 11.4),  # Conecta o nó 0 ao nó 1
    (1, 2, 26.1),
    (2, 4, 30.0),  # Conecta o nó 1 ao nó 2
    (1, 3, 30.0),  # Conecta o nó 2 ao nó 3
    (3, 4, 25.9),  # Conecta o nó 3 ao nó 4
    (4, 5, 27.1),  # Conecta o nó 4 ao nó 5
    (5, 6, 21.0),  # Conecta o nó 5 ao nó 6
    (6, 3, 60.0),
    (6, 7, 60.0),  # Conecta o nó 6 ao nó 3
    (7, 0, 60.0),  # Conecta o nó 6 ao nó 0, formando o ciclo
]

# Inicializar o grafo e as distâncias
grafo = {}
distancia = [float('inf')] * N  # Distâncias inicialmente infinitas
visitado = [False] * N  # Vetor de nós visitados
anterior = [-1] * N  # Para armazenar o caminho anterior

# Passo 2: Inicializar o Grafo
for i in range(N):
    grafo[i] = {}

# Adicionar as arestas e os pesos ao grafo
for origem, destino, peso in arestas:
    grafo[origem][destino] = peso
    grafo[destino][origem] = peso  # Se o grafo for não-direcionado

# Definir a origem e o destino
source = 0  # Definimos o nó de origem
target = 6  # Definimos o nó objetivo
distancia[source] = 0  # A distância da origem para si mesmo é 0

# Fila de prioridade para o próximo nó a ser processado
fila_prioridade = [(0, source)]  # Inicia com a distância da origem para si mesmo (0)

# Implementação do Dijkstra
while fila_prioridade:
    dist_u, u = heapq.heappop(fila_prioridade)  # Remove o nó com a menor distância
    if visitado[u]:
        continue

    visitado[u] = True  # Marca o nó como visitado

    # Atualiza as distâncias dos vizinhos do nó u
    for v, peso in grafo[u].items():
        if not visitado[v] and dist_u + peso < distancia[v]:
            distancia[v] = dist_u + peso
            anterior[v] = u  # Armazena o nó anterior para reconstruir o caminho
            heapq.heappush(fila_prioridade, (distancia[v], v))  # Adiciona o nó à fila

# Reconstruir o menor caminho do objetivo até a origem
path = []
current_node = target
while current_node != -1:
    path.append(current_node)
    current_node = anterior[current_node]

path = path[::-1]  # Inverter para obter o caminho correto (do source ao target)

# Exibir o Resultado
print(f"Menores distâncias a partir do nó {source}:")
for i in range(N):
    print(f"Distância até o nó {i}: {distancia[i]}")

print(f"\nCaminho do nó {source} até o nó {target}: {path}")

# Visualização do Grafo
G = nx.Graph()

for u in grafo:
    for v, peso in grafo[u].items():
        G.add_edge(u, v, weight=peso)

# Definir posições para criar dois quadrados
pos = {
    0: (0, 0),
    1: (1, 0),
    2: (2, 0),
    3: (1, -1),
    4: (2, -1),
    5: (2, -2),
    6: (1, -2),
    7: (0, -2),
}

# Desenhar o grafo com as posições definidas
nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=12, font_weight="bold")
weights = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edges(G, pos, width=[w / 2 for w in weights.values()], edge_color='gray')

# Desenhar os rótulos das arestas (distâncias)
nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)

# Destaque o caminho mínimo em vermelho
path_edges = list(zip(path[:-1], path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

# Mostrar o gráfico
plt.title("Grafo com Distâncias e Caminho Mínimo (Dois Quadrados)")
plt.show()
