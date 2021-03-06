from random import randint
from time import time

def timeMeasure(func):
	def wrapper(arr):
		start = time()
		result = func(arr)
		stop = time()
		return {'result':result, 'time': stop - start}
	wrapper.__name__ = func.__name__	
	return wrapper

#select sort
@timeMeasure
def selectSortMin(arr):
	for i in range(len(arr) - 1):
		m = min(arr[i:])
		push = arr[i]
		arr[arr[i:].index(m) + i] = push
		arr[i] = m	
	return arr

@timeMeasure
def selectSortMax(arr):
	for i in range(-1, -len(arr), -1):
		m = max(arr[:i])
		if m > arr[i]:
			push = arr[i]
			arr[arr.index(m)] = push
			arr[i] = m
	return arr

# insert sort
@timeMeasure
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
@timeMeasure
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
@timeMeasure
def mergeSort(arr):
	def msort(arr):
		n = len(arr) // 2
		if not n: return arr

		m1 = msort(arr[:n])
		m2 = msort(arr[n:])
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
	ans = msort(arr)
	return ans

# quick sort
@timeMeasure
def quickSort(arr):
	start, stop = 0, len(arr) - 1

	def qsort(arr, start, stop):
		if start < stop:
			pivot = partition(arr, start, stop)
			qsort(arr, start, pivot - 1)
			qsort(arr, pivot + 1, stop)
		return arr

	def partition(arr, start, stop):
		pivot = randint(start, stop - 1)
		arr[stop], arr[pivot] = arr[pivot], arr[stop]
		pI = start - 1
		for i in range(start, stop):
			if arr[i] <= arr[stop]:
				pI += 1
				arr[i], arr[pI] = arr[pI], arr[i]
		arr[pI + 1], arr[stop] = arr[stop], arr[pI + 1]
		return pI + 1
	arr = qsort(arr, start, stop)
	return arr




