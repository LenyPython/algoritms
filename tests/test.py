from random import randint
# test cases

#check if the array is sorted
def checkIfSorted(arr):
	return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

# test function
def test(*args):
	#	testcase = input('Choose test size: 0, 1, 2, 3')
	TESTS = {
			'0.tiny': [randint(0,19) for _ in range(10)],
			#'1.small': [randint(0, 200) for _ in range(100)],
			#'2.medium': [randint(0,10000) for _ in range(5000)],
			#'3.big': [randint(0,10000) for _ in range(10000)]
			}
	for func in args:
		print(f'Running tests for: {func.__name__}\n')
		for key, case in TESTS.items():
			sortedArray = func(case)
			result = checkIfSorted(sortedArray)
			print(f'Test case: {key}, result: {result}')
		print('...................................\n')
		




