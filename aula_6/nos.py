import networkx as nx
import matplotlib.pyplot as plt

# Criar um grafo com NetworkX
G = nx.Graph()

# Adicionar nós (opcional, o NetworkX adiciona nós automaticamente ao adicionar arestas)
# Vamos adicionar as arestas com os pesos (distâncias)

# Arestas do grafo (origem, destino, peso)
arestas = [
    (0, 1, 10),  # Distância 10 entre o nó 0 e 1
    (0, 2, 5),   # Distância 5 entre o nó 0 e 2
    (1, 2, 2),   # Distância 2 entre o nó 1 e 2
    (1, 3, 1),   # Distância 1 entre o nó 1 e 3
    (2, 3, 9),   # Distância 9 entre o nó 2 e 3
    (3, 4, 4)    # Distância 4 entre o nó 3 e 4
]

# Adicionar as arestas com os pesos ao grafo
for origem, destino, peso in arestas:
    G.add_edge(origem, destino, weight=peso)

# Pegar as posições dos nós para desenhar o grafo (usamos spring_layout para ter uma disposição clara)
pos = nx.spring_layout(G)

# Desenhar os nós
nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=12, font_weight="bold")

# Desenhar as arestas com os pesos (largura das arestas proporcional ao peso)
weights = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edges(G, pos, width=[w / 2 for w in weights.values()], edge_color='gray')

# Desenhar os rótulos das arestas (distâncias)
nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)

# Mostrar o gráfico
plt.title("Grafo com Distâncias nas Arestas")
plt.show()
