
#select sort
def selectSortMin(arr):
	for i in range(len(arr) - 1):
		m = min(arr[i:])
		push = arr[i]
		arr[arr[i:].index(m) + i] = push
		arr[i] = m	
	return arr

def selectSortMax(arr):
	print(arr)
	for i in range(-1, -len(arr), -1):
		m = max(arr[:i])
		push = arr[i]
		arr[arr.index(m)] = push
		arr[i] = m
		print(f'index: {i}, max: {m}, sub: {arr[:i]}, array: {arr})')
	print(arr)
	return arr

# insert sort
def insertSort(arr):
	for i,v in enumerate(arr):
		if i + 1 < len(arr):
			if v > arr[i + 1]:
				arr[i], arr[i + 1] = arr[i + 1], arr[i]
		while i and arr[i] < arr[i - 1]:
			arr[i], arr[i - 1] = arr[i - 1], arr[i]
			i -= 1
	return arr

#merge sort

# heep sort
