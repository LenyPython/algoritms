from random import randint



# test cases
testcases = {
			'1.small': [randint(0,10000) for _ in range(10000)],
			'2.medium': [randint(0,10000) for _ in range(5000)],
			'3.big': [randint(0,10000) for _ in range(100)]
			}

# test function
def checkIfSorted(arr):
	return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def test(tests, *funcs):
	for func in funcs:
		print(f'Running tests for: {func.__name__}\n')
		for key, case in tests.items():
			sortedArray = func(case)
			result = checkIfSorted(sortedArray)
			print(f'Test case: {key}, result: {result}')
		print('...................................\n')

#select sort
def selectSortMin(arr):
	
	return arr

def selectSortMax(arr):

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
