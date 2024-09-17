import heapq
import networkx as nx
import matplotlib.pyplot as plt

#Passo 1: Declaração de Variáveis e Entrada de Dados
"""var
   N, M, origem, destino, i, j, u, v : inteiro
   distancia : vetor[1..100] de inteiro
   visitado : vetor[1..100] de logico
   grafo : vetor[1..100, 1..100] de inteiro
   peso, menorDistancia : inteiro"""

N = int(input("Digite o número de nós (N): "))
M = int(input("Digite o número de arestas (M): "))

grafo = {}
distancia = [float('inf')] * N  # Distâncias inicialmente infinitas
visitado = [False] * N  # Vetor de nós visitados

#Passo 2: Inicialização do Grafo
"""// Inicializar o grafo com infinito (ou um valor grande)
para i de 1 ate N faca
   para j de 1 ate N faca
      grafo[i, j] <- 999999  // Definimos um valor grande para representar "infinito"
fimpara
fimpara"""
# Inicializar o grafo
for i in range(N):
    grafo[i] = {}

# Ler as arestas e adicionar os pesos
for _ in range(M):
    origem, destino, peso = map(int, input("Digite a aresta (origem, destino, peso): ").split())
    grafo[origem][destino] = peso
    grafo[destino][origem] = peso  # Se o grafo for não-direcionado

#Passo 3: Inicializar o Vetor de Distâncias e de Visitados
"""// Inicializar as distâncias e o vetor de visitados
para i de 1 ate N faca
   distancia[i] <- 999999  // Infinito
   visitado[i] <- falso
fimpara"""

#distancia = [float('inf')] * N  # Inicialmente todas as distâncias são infinitas
#visitado = [False] * N  # Nenhum nó foi visitado ainda

#Passo 4: Definir a Origem e Inicializar o Algoritmo
"""// Definir a distância do nó de origem para ele mesmo como 0
distancia[origem] <- 0"""

origem = int(input("Digite o nó de origem: "))
distancia[origem] = 0  # A distância da origem para si mesmo é 0

#Passo 5: O Algoritmo Principal de Dijkstra
"""para i de 1 ate N faca
   // Encontre o nó não visitado com a menor distância
   menorDistancia <- 999999
   u <- -1
   para j de 1 ate N faca
      se (visitado[j] = falso) e (distancia[j] < menorDistancia) entao
         menorDistancia <- distancia[j]
         u <- j
      fimse
   fimpara

   // Se não encontrou nenhum nó, finaliza
   se (u = -1) entao
      pare
   fimse

   // Marca o nó u como visitado
   visitado[u] <- verdadeiro

   // Atualiza as distâncias dos vizinhos do nó u
   para v de 1 ate N faca
      se (visitado[v] = falso) e (grafo[u, v] <> 999999) entao
         se (distancia[u] + grafo[u, v] < distancia[v]) entao
            distancia[v] <- distancia[u] + grafo[u, v]
         fimse
      fimse
   fimpara
fimpara
"""

# Fila de prioridade para o próximo nó a ser processado
fila_prioridade = [(0, origem)]  # Inicia com a distância da origem para si mesmo (0)

while fila_prioridade:
    dist_u, u = heapq.heappop(fila_prioridade)  # Remove o nó com a menor distância
    if visitado[u]:
        continue

    visitado[u] = True  # Marca o nó como visitado

    # Atualiza as distâncias dos vizinhos do nó u
    for v, peso in grafo[u].items():
        if not visitado[v] and dist_u + peso < distancia[v]:
            distancia[v] = dist_u + peso
            heapq.heappush(fila_prioridade, (distancia[v], v))  # Adiciona o nó à fila

#Passo 6: Exibir o Resultado
"""// Exibe as menores distâncias do nó de origem para todos os outros nós
escreva("Menores distâncias a partir do nó ", origem, ":")
para i de 1 ate N faca
   escreva("Distância até o nó ", i, ": ", distancia[i])
fimpara"""

print(f"Menores distâncias a partir do nó {origem}:")
for i in range(N):
    print(f"Distância até o nó {i}: {distancia[i]}")

G = nx.Graph()

for u in grafo:
    for v, peso in grafo[u].items():
        G.add_edge(u, v, weight=peso)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=12, font_weight="bold")
weights = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edges(G, pos, width=[w / 2 for w in weights.values()], edge_color='gray')

# Desenhar os rótulos das arestas (distâncias)
nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)

# Mostrar o gráfico
plt.title("Grafo com Distâncias nas Arestas")
plt.show()


