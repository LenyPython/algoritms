from random import randint
from alg.sortingalgs import quickSort, mergeSort, bubbleSort, insertSort, selectSortMin, selectSortMax


#check if the array is sorted
def checkIfSorted(arr):
	return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def createTest(size):
	return [randint(0,size) for _ in range(size)]

# test function
def test(size, repeat, *args):
	#	testcase = input('Choose test size: 0, 1, 2, 3')
	TESTS = {
			'1': createTest(10),
			'2': createTest(100),
			'3': createTest(1000),
			'4': createTest(10000)
			}

	sortingAlgorithms = {
			'1':quickSort,
			'2':mergeSort,
			'3':bubbleSort,
			'4':insertSort,
			'5':selectSortMin,
			'6':selectSortMax
			}
	
	for key in args:
		for s in size:
			for time in range(1, repeat + 1):
				print(f'Running tests for: {sortingAlgorithms[key].__name__}. Test no. {time}\n')
				sortedArray = sortingAlgorithms[key](TESTS[s])
				# sortedArray is a dictionary with sorted arr and time
				# keys are result -> sorted array, time -> time elapsed
				result = checkIfSorted(sortedArray['result'])
				#time spent on testes t
				t = sortedArray['time']
				print(f'Test case {size} is sorted: {result}, in: {t:.6f} sec')
			print('...................................\n')
		




