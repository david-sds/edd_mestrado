#linear search
def linear_search(arr, element):
    for i, num in enumerate(arr):
        if num == element:
            return i
    return -1