from generator.generator import generateMaze, backtrack
from pathfinder.findpaths import find_paths, show_paths
import numpy as np
import time


def userInput():
	n = ''
	while not n.isdigit() or n == '0':
		n = input('Choose a maze size (n x n) 1-15: ')
		if not n.isdigit() or n == '0':	print('!!! WRONG INPUT !!!')
		else:
			if int(n) > 15:
				n = ''
				print('!!!To big number!!!')
	return int(n)	

def main():
	n = userInput()
	size = n - 1
	mainMaze = generateMaze(n)
	print('Generating maze... ')
	while not backtrack(mainMaze, size):
		mainMaze = generateMaze(n)
	print(mainMaze)
	print(f'Has a solution: {backtrack(mainMaze, size)}')
	
	paths = find_paths(mainMaze, size)
	show_paths(paths)


if __name__ == '__main__':
	main()

