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
		sortedCase = insertSort(case)
		result = all(sortedCase[i] <= sortedCase[i + 1] for i in range(len(sortedCase) - 1))
		print(f'Test no. {i}, result for insertSort: {result}')	


# insert sort
def insertSort(arr):
	for i,v in enumerate(arr):
		if i + 1 < len(arr):
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
