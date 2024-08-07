import numpy as np
import time
import random

def selection_sort(arr):
	res = [0, 0]
	arr_size = len(arr)
	for i in range(arr_size):
		minimum_index = i
		for j in range(arr_size - i):
			res[0] = res[0] + 1
			if arr[j + i] < arr[minimum_index]:
				minimum_index = j + i
		arr[i], arr[minimum_index] = arr[minimum_index], arr[i]
		res[1] = res[1] + 1
	return res


def quick_sort(arr, low, high, res):
	if low < high:
		pivot = partition(arr, low, high, res)

		quick_sort(arr, low, pivot - 1, res)
		quick_sort(arr, pivot + 1, high, res)
def partition(arr, low, high, res):
	pivot = arr[high]
	i = low - 1
	for j in range(low, high):
		res[0] = res[0] + 1
		if arr[j] < pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
			res[1] = res[1] + 1
	i += 1
	arr[i], arr[high] = arr[high], arr[i]
	res[1] = res[1] + 1
	return i

def linear_search(arr, element):
    for i, num in enumerate(arr):
        if num == element:
            return i
    return -1

def binary_search(arr, low, high, element):
	test_index = round(low + (high - low) / 2)
	test = arr[test_index]
	if element == test:
		return test_index
	if element < test:
		return binary_search(arr, low, test_index - 1, element)
	return binary_search(arr, test_index + 1, high, element)


seeds = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for seed in seeds:
	random.seed(seed)
	np.random.seed(seed)
	print(f'USING SEED {seed}')
	sizes = [50, 500, 5000, 10000, 20000]
	for size in sizes:
		#Sorteia 'size' elements
		arr = np.random.randint(0, 99999, size)

		# Ordenar o vetor
		sorted_arr = arr.copy()

		start_time = time.time()
		res = selection_sort(arr.copy())
		end_time = time.time()
		selection_sort_time = end_time - start_time
		selection_sort_iterations = res[0]
		selection_sort_switches = res[1]

		res = [0, 0]
		start_time = time.time()
		quick_sort(sorted_arr, 0, len(arr) - 1, res)
		end_time = time.time()
		quick_sort_time = end_time - start_time
		quick_sort_iterations = res[0]
		quick_sort_switches = res[1]


		# Para garantir que o valor vai existir, seleciona um número aleatório presente no vetor
		target_element = np.random.choice(arr)

		# Medir o tempo para encontrar o elemento no vetor desordenado (busca linear)
		start_time = time.time()
		index_linear_unsorted = linear_search(arr, target_element)
		end_time = time.time()
		linear_unsorted_search_time = end_time - start_time

		# Medir o tempo para encontrar o elemento no vetor ordenado (busca linear)
		start_time = time.time()
		index_linear_sorted = linear_search(sorted_arr, target_element)
		end_time = time.time()
		linear_sorted_search_time = end_time - start_time


		# Medir o tempo para encontrar o elemento no vetor ordenado (busca binária)
		start_time = time.time()
		index_binary = binary_search(sorted_arr, 0, len(sorted_arr) - 1, target_element) #ESSA FUNCAO DEVERÁ SER IMPLEMENTADA NO TRABALHO
		end_time = time.time()
		binary_search_time = end_time - start_time

		# Resultados
		print('\n___________________________________________\n')
		print('RESULTADOS:')
		print(f"Tamanho Array: {len(arr)} (min: {sorted_arr[0]}, max: {sorted_arr[-1]})")

		print("\n>>> Ordenação")
		print("Selection Sort")
		print(f" - Tempo: {selection_sort_time:.10f} segundos")
		print(f" - Iterações: {selection_sort_iterations}")
		print(f" - Trocas: {selection_sort_switches}")
		print("Quick Sort")
		print(f" - Tempo: {quick_sort_time:.10f} segundos")
		print(f" - Iterações: {quick_sort_iterations}")
		print(f" - Trocas: {quick_sort_switches}")

		print("\n>>> Busca")
		print(f" - Elemento: {target_element}")
		print('Busca linear (Lista desordenada):')
		print(f" - Index: {index_linear_unsorted}")
		print(f" - Tempo: {linear_unsorted_search_time:.10f} segundos")
		print('Busca linear (Lista ordenada):')
		print(f" - Index: {index_linear_sorted}")
		print(f" - Tempo: {linear_sorted_search_time:.10f} segundos")
		print('Busca binária (Lista ordenada):')
		print(f" - Index: {index_binary}")
		print(f" - Tempo: {binary_search_time:.10f} segundos")