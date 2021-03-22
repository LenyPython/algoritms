from tests.test import test, checkIfSorted

def userInput():
		print('Choose a sorting algoritm/s: ')
		print('1.quickSort 2.mergeSort 3.bubbleSort ')
		print('4.insertSort 5.selectSortMin 6.selectSortMax ')
		algorithm = input('ALL for all ')
		print('Which test would you like to run? ')
		case = input('1. tiny 2. small 3. medium 4. big a. all ')
		repeat = int(input('How many repeats? '))

		if algorithm == 'all' or algorithm == 'ALL':
			algorithm = ['1', '2', '3', '4', '5', '6']
		else:
			algorithm = [size for size in algorithm if size.isdigit()]

		if case == 'all' or case == 'ALL':
			case = ['1', '2', '3', '4']
		else:
			case = [size for size in case if size.isdigit()]
		return {'alg': algorithm, 'size': case, 'times': repeat }

# main I/O function for running specific tests
def main():
	run = True
	while run:
		print('\nSorting algoritm tester')
		choice = userInput()
		
		# run test function with chosen allgorithms
		# takes list size, times of repeat and choosen algorithms and *args
		test(choice['size'], choice['times'], choice['alg'])

		cont = input('Would you like to take another test? y/n')
		while cont != 'y' and cont != 'n':
			cont = input('Wrong input, run? y/n ')
		if cont == 'n': break

if __name__ == '__main__':

	main()



