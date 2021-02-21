from random import randint



# test cases
testcases = {
			'small': [randint(0,10000) for _ in range(10000)],
			'medium': [randint(0,10000) for _ in range(5000)],
			'big': [randint(0,10000) for _ in range(100)]
			}

# test function
def checkIfSorted(arr):
	return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def test(tests, *funcs):
	for func in funcs:
		print('Running tests ...')
		for key, case in tests.items():
			sortedArray = func(case)
			result = checkIfSorted(sortedArray)
			print(f'Test case: {key}, result for insertSort: {result}')	

#select sort
def selectSortMin(arr):
	for i in range(len(arr)):
		index = arr.index(min(arr[i:]))
		arr[i], arr[index] = arr[index], arr[i]
	return arr
def selectSortMax(arr):
	for i in range(0, len(arr), -1):
		index = arr.index(max(arri[:i]))
		arr[i], arr[index] = arr[index], arr[i]
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

if __name__ == '__main__':
	test(testcases, selectSortMin, selectSortMax, insertSort)
