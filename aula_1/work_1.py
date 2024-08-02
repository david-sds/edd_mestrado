import numpy as np
import time
import random
import bisect #nao pode ser usada no trabalho

# Definir a seed para garantir reproducibilidade
random.seed(42)
np.random.seed(42)

def selection_sort(arr):
	arr = arr.copy()
	arr_size = len(arr)
	for i in range(arr_size):
		minimum_index = i
		for j in range(arr_size - i):
			if arr[j + i] < arr[minimum_index]:
				minimum_index = j + i
		arr[i], arr[minimum_index] = arr[minimum_index], arr[i]
	return arr;


def linear_search(arr, element):
    for i, num in enumerate(arr):
        if num == element:
            return i
    return -1
        

size = 10  # Tamanho do vetor

#Sorteia 'size' elements 
arr = np.random.randint(-99999999, 99999999, size)

# Ordenar o vetor
sorted_arr = selection_sort(arr) #deverá ser implementa no trabalho
print('arr', arr)
print('sorted_arr', sorted_arr)

# Para garantir que o valor vai existir, seleciona um número aleatório presente no vetor 
target_element = np.random.choice(arr)

# # Medir o tempo para encontrar o elemento no vetor desordenado (busca linear)
# start_time = time.time()
# index_linear_unsorted = linear_search(arr, target_element)
# end_time = time.time()
# linear_unsorted_search_time = end_time - start_time

# # Medir o tempo para encontrar o elemento no vetor ordenado (busca linear)
# start_time = time.time()
# index_linear_sorted = linear_search(sorted_arr, target_element)
# end_time = time.time()
# linear_sorted_search_time = end_time - start_time


# # Medir o tempo para encontrar o elemento no vetor ordenado (busca binária)
# start_time = time.time()
# index_binary = bisect.bisect(sorted_arr, target_element) #ESSA FUNCAO DEVERÁ SER IMPLEMENTADA NO TRABALHO
# end_time = time.time()
# binary_search_time = end_time - start_time

# # Resultados
# print(f"Tam Array {len(arr)} - Min: {sorted_arr[0]} - Max: {sorted_arr[-1]}")
# print(f"Elemento: {target_element}")
# print(f"Índice do elemento (busca linear - unsorted): {index_linear_unsorted}")
# print(f"Tempo para encontrar no vetor desordenado (busca linear): {linear_unsorted_search_time:.10f} segundos\n\n")

# print(f"Índice do elemento (busca linear - sorted): {index_linear_sorted}")
# print(f"Tempo para encontrar no vetor ordenado (busca linear): {linear_sorted_search_time:.10f} segundos\n\n")

# print(f"Índice do elemento (busca binária): {index_binary-1}") #Ajustando o index de 1 ... N, para 0 ... N-1
# print(f"Tempo para encontrar no vetor ordenado (busca binária): {binary_search_time:.10f} segundos")