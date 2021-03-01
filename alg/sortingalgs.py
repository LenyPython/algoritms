
#select sort
def selectSortMin(arr):
	for i in range(len(arr) - 1):
		m = min(arr[i:])
		push = arr[i]
		arr[arr[i:].index(m) + i] = push
		arr[i] = m	
	return arr

def selectSortMax(arr):
	for i in range(-1, -len(arr), -1):
		m = max(arr[:i])
		if m > arr[i]:
			push = arr[i]
			arr[arr.index(m)] = push
			arr[i] = m
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

# bubble sort
def bubbleSort(arr):
	n = len(arr)
	for i in range(n):
		isSorted = True
		for j in range(n - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j],arr[j + 1] = arr[j + 1], arr[j]
				isSorted = False
		if isSorted: break
	return arr

# merge sort
def mergeSort(arr):
	n = len(arr) // 2
	if not n: return arr

	m1 = mergeSort(arr[:n])
	m2 = mergeSort(arr[n:])
	# merge part
	i, j, k  = 0, 0, 0

	while i < len(m1) and j < len(m2):
		if m1[i] <= m2[j]:
			arr[k] = m1[i]
			i += 1
			k += 1
		else:
			arr[k] = m2[j]
			k += 1
			j += 1
	while i < len(m1):
		arr[k] = m1[i]
		i += 1
		k += 1
	while j < len(m2):
		arr[k] = m2[j]
		j += 1
		k += 1
	return arr




