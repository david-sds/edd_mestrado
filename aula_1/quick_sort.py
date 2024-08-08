#quick sort
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

