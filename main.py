from tests.test import test, checkIfSorted
from alg.sortingalgs import *

# main I/O function for running specific tests
def main():
	while True:
		print('Sorting algoritm tester')
		algoritm = input('Choose a sorting algoritm/s (for all write all):')
		case = input('which test would you like to run?\n \
			(tiny, small, medium, big, all)')
		
		# run test function with chosen allgorithms
		test()
		run = input('Would you like to take another test? y/n')
		if run != 'y' and run != 'n':
			run = input('Wrong input, run? y/n')
		if run == 'n': break


if __name__ == '__main__':
	 test(quickSort, bubbleSort, insertSort, selectSortMin, selectSortMax)
