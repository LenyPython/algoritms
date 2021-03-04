from random import randint

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
	k  = 0

	while m1 and m2:
		if m1[0] <= m2[0]:
			arr[k] = m1.pop(0)
		else:
			arr[k] = m2.pop(0)
		k += 1

	while m1:
		arr[k] = m1.pop(0)
		k += 1
	while m2:
		arr[k] = m2.pop(0)
		k += 1
	return arr

# quick sort
def quickSort(arr, start, stop):
	print(arr)

	def partition(arr, start, stop):
		pivot = arr[randint(start, stop)]
		arr[stop], pivot = pivot, arr[stop]
		pI = start - 1
		for i in range(start, stop):
			if arr[i] <= pivot:
				arr[i], arr[pI] = arr[pI], arr[i]
				pI += 1
		arr[pI + 1], arr[stop] = arr[stop], arr[pI + 1]
		return pI

	if start < stop:
		pivot = partition(arr, start, stop)
		quickSort(arr, start, pivot)
		quickSort(arr, pivot + 1, stop)
	print(arr)
	return arr

arr = [randint(1,20) for _ in range(10)]

quickSort(arr, 0, len(arr) - 1)



