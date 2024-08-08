# Selection Sort
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