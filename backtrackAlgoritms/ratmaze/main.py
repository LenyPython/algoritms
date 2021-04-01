from generator.generator import generateMaze
from pathfinder.findpaths import findPaths
import numpy as np
import time


def backtrack(maze, i = 0, j = 0, came_from=None):
	time.sleep(0.1)
	n = len(maze) - 1
	if i == n and j == n: return True
	if i <= n and j <= n:
		if maze[i][j]:
			print([i, j], maze[i][j])
			if came_from != 'down':
				if backtrack(maze, i + 1, j, 'top'): return True
			if came_from != 'right':
				if backtrack(maze, i, j + 1, 'left'): return True
			if came_from != 'top':
				if i > 0 and j > 1:
					if not maze[i - 1][j - 1]:
						if backtrack(maze, i - 1, j, 'down'): return True
			if came_from != 'left':
				if i > 1 and j > 0:
					if not maze[i - 1][j - 1] or not maze[i][j - 1]:
						if backtrack(maze, i, j - 1, 'right'): return True
			return False

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
	print(f'Has a solution: {backtrack(mainMaze)}')
#	while not backtrack(mainMaze):
#		mainMaze =generateMaze(n)
#		print(mainMaze)
#		print(f'Has a solution: {backtrack(mainMaze)}')


if __name__ == '__main__':
	main()

