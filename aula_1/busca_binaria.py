#binary search
def binary_search(arr, low, high, element):
	test_index = round(low + (high - low) / 2)
	test = arr[test_index]
	if element == test:
		return test_index
	if element < test:
		return binary_search(arr, low, test_index - 1, element)
	return binary_search(arr, test_index + 1, high, element)