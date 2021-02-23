from tests.test import test, checkIfSorted

def main():
	while True:
		print('Sorting algoritm tester')
		algoritm = input('Choose a sorting algoritm/s (for all write all):')
		test = input('which test would you like to run?\n
			(tiny, small, medium, big, all)')

		test()
		continue = input('Would you like to take another test? y/n')
		if continue != 'y' and continue != 'n':
			continue = input('Wrong input, continue? y/n')
		if continue == 'n': break


if __name__ == '__main__':
	test(insertSort, selectSortMin, selectSortMax)
