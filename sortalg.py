from random import randint



# test cases
smallList = [randint(0,10000) for _ in range(100)]
mediumList = [randint(0,10000) for _ in range(5000)]
bigList = [randint(0,10000) for _ in range(10000)]
testcases = [smallList, mediumList, bigList]

# test function
def test(tests):
	print('Running tests ...')
	for i, case in enumerate(tests):
		print(f'Test no. {i}, result for insertSort:{insertSort(case)}')	


# insert sort
def insertSort(arr):
	for i,v in enumerate(arr):
		if v > arr[i + 1]:
			arr[i], arr[i + 1] = arr[i + 1], arr[i]
		while i:
			if arr[i] < arr[i - 1]:
				arr[i], arr[i - 1] = arr[i - 1], arr[i]
			i -= 1
	return arr

#merge sort

# heep sort

if __name__ == '__main__':
	test(testcases)
