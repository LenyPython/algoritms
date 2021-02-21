from random import randint



# test cases
smallList = [randint(0,10000) for _ in range(100)]
mediumList = [randint(0,10000) for _ in range(5000)]
bigList = [randint(0,10000) for _ in range(10000)]
testcases = {'small': smallList, 'medium': mediumList, 'big': bigList}

# test function
def test(tests):
	print('Running tests ...')
	for key,item in tests.items():
		sortedCase = insertSort(item)
		result = all(sortedCase[i] <= sortedCase[i + 1] for i in range(len(sortedCase) - 1))
		print(f'Test case: {key}, result for insertSort: {result}')	


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
	test(testcases)
