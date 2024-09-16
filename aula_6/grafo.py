import networkx as nx
import matplotlib.pyplot as plt
import random

# Nomes de ruas e avenidas
horizontal_streets = ["Rua A", "Rua B", "Rua C", "Rua D", "Rua E", "Rua F"]  # Uma rua para cada linha
vertical_streets = ["Av. 1", "Av. 2", "Av. 3", "Av. 4", "Av. 5", "Av. 6"]  # Uma avenida para cada coluna

rows = 6
cols = 6

# Criar o grafo
G = nx.Graph()

# Adicionar nós
for i in range(rows):
    for j in range(cols):
        node_id = i * cols + j + 1
        G.add_node(node_id, pos=(j, -i))  # Posição dos nós

# Adicionar arestas com pesos aleatórios (simbolizando diferentes comprimentos de ruas e avenidas)
for i in range(rows):
    for j in range(cols):
        node_id = i * cols + j + 1
        # Aresta para a direita (ruas horizontais)
        if j < cols - 1:
            street_name = horizontal_streets[i]  # Nome da rua horizontal
            street_length = random.randint(50, 300)  # Comprimento aleatório em metros
            G.add_edge(node_id, node_id + 1, weight=street_length, street=street_name)
        
        # Aresta para baixo (avenidas verticais)
        if i < rows - 1:
            street_name = vertical_streets[j]  # Nome da avenida vertical
            avenue_length = random.randint(50, 300)  # Comprimento aleatório em metros
            G.add_edge(node_id, node_id + cols, weight=avenue_length, street=street_name)

# Pegar as posições dos nós
pos = nx.get_node_attributes(G, 'pos')

# Pegar os pesos das arestas para ajustar a largura
weights = nx.get_edge_attributes(G, 'weight')

# Definir a espessura das arestas (inverter a lógica)
# Mais espessa para ruas mais curtas, mais fina para ruas mais longas
max_width = 10
min_width = 1
edge_widths = [max_width - (weights[edge] / 300) * (max_width - min_width) for edge in G.edges]

# Encontrar o caminho mínimo
source = 1
target = 22
path = nx.dijkstra_path(G, source=source, target=target, weight='weight')
path_edges = list(zip(path[:-1], path[1:]))

# Calcular o deslocamento total pelo caminho de Dijkstra
total_distance = sum(weights[edge] for edge in path_edges)

# Exibir o deslocamento total
print(f"Deslocamento total pelo caminho escolhido pelo Dijkstra: {total_distance} metros")

# Desenhar o grafo e o caminho mínimo
nx.draw(G, pos, with_labels=True, node_size=300, node_color="lightgreen", font_size=8, font_weight="bold")

# Ajustar a espessura das arestas de acordo com os pesos (agora mais comprida = mais fina)
nx.draw_networkx_edges(G, pos, width=edge_widths, edge_color='gray')
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

# Adicionar rótulos de distância (comprimento) nas arestas
edge_labels = {edge: f"{weights[edge]} m" for edge in G.edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

# Adicionar os nomes das avenidas na primeira linha (acima da grade)
for j in range(cols):
    x_position = j  # Posição horizontal da avenida
    y_position = 0.1  # Colocar o nome acima da primeira linha
    plt.text(x_position, y_position, vertical_streets[j], horizontalalignment='center', verticalalignment='center', fontsize=10, color='red')

# Adicionar os nomes das ruas à esquerda da primeira coluna
for i in range(rows):
    x_position = -0.15  # Colocar o nome à esquerda da primeira coluna
    y_position = -i  # Posição vertical ao lado da linha correspondente
    plt.text(x_position, y_position, horizontal_streets[i], horizontalalignment='center', verticalalignment='center', fontsize=10, color='blue')

# Mostrar o gráfico com o título
plt.title(f"Rede de Iluminação Pública com Caminho Mínimo (Total: {total_distance} metros)")
plt.grid(False)
plt.show()
