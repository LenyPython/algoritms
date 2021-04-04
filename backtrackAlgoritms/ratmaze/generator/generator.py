import numpy as np
from random import randint

def generateMaze(n):
	maze = np.array([[randint(0,1) for _ in range(n)] for _ in range(n)])
	maze[0][0], maze[-1][-1] = 1, 1
	return maze

def backtrack(maze, n, i = 0, j = 0, came_from=None):
	if i == n and j == n: return True
	if i <= n and j <= n:
		if maze[i][j]:
			if came_from != 'down':
				if backtrack(maze, n, i + 1, j, 'top'): return True
			if came_from != 'right':
				if backtrack(maze, n, i, j + 1, 'left'): return True
			if came_from != 'top':
				if i > 0 and j > 1:
					if not maze[i - 1][j - 1]:
						if backtrack(maze, n, i - 1, j, 'down'): return True
			if came_from != 'left':
				if i > 1 and j > 0:
					if not maze[i - 1][j - 1] or not maze[i][j - 1]:
						if backtrack(maze, n, i, j - 1, 'right'): return True
			return False



	
