from generator.generator import generateMaze
from pathfinder.findpaths import findPaths
import numpy as np


def backtrack(maze, n, i = 0, j = 0, goDown = True, goRight = True):
	if i == n and j == n: return True
	if i <= n and j <= n:
		if maze[i][j]:
			print([i, j], maze[i][j])
			up, down, left, right = False, False, False, False
			if goDown:
				down = backtrack(maze, i + 1, j, n)
			if goRight:
				right = backtrack(maze, i, j + 1, n)
			if i > 0 and j > 1:
				if not maze[i - 1][j - 1]:
					up = backtrack(maze, i - 1, j, n, False, True)
			############# debug
			if i > 1 and j > 0:
				if not maze[i - 1][j - 1] or not maze[i][j - 1]:
					left = backtrack(maze, i, j - 1, n, True, False)
			return True if any([up, down, left, right]) else False

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
	arrLen = n - 1
	#mainMaze = generateMaze(n)
	mainMaze = np.array(
				[[1,1,0,1,1,1],
				[0,1,1,1,0,1],
				[0,0,0,0,1,1],
				[0,1,1,1,1,0],
				[0,1,0,0,0,0],
				[0,1,1,1,1,1]]
				)
				
	print(mainMaze)
	print(f'Has a solution: {backtrack(mainMaze, arrLen)}')
#	while not backtrack(mainMaze, arrLen):
#		mainMaze =generateMaze(n)
#		print(mainMaze)
#		print(f'Has a solution: {backtrack(mainMaze, arrLen)}')


if __name__ == '__main__':
	main()

