from tests.test import test, checkIfSorted
from alg.sortingalgs import quickSort, mergeSort, bubbleSort, insertSort, selectSortMin, selectSortMax

sortingAlgorithms = {
		'1':quickSort,
		'2':mergeSort,
		'3':bubbleSort,
		'4':insertSort,
		'5':selectSortMin,
		'6':selectSortMax
		}

def userInput():
		algoritm = input('Choose a sorting algoritm/s: \n \
						1.quickSort 2.mergeSort 3.bubbleSort\n \
						4.insertSort 5.selectSortMin 6.selectSortMax\n \
						ALL for all' )
		case = input('which test would you like to run?\n \
			1. tiny 2. small 3. medium 3. big a. all)')
		repeat = input('How many repeats? ')
		return {'alg': algorithm, 'size': case, 'times': repeat }

# main I/O function for running specific tests
def main():
	run = True
	while run:
		print('Sorting algoritm tester')
		choice = userInput()
		
		# run test function with chosen allgorithms
		# takes list size, times of repeat and choosen algorithms and *args
		test(choice['size'], choice['times'], sortingAlgorithms[choice['alg']])

		cont = input('Would you like to take another test? y/n')
		while cont != 'y' and cont != 'n':
			cont = input('Wrong input, run? y/n')
		if cont == 'n': break


if __name__ == '__main__':
	 test(sortingAlgorithms['4'])
