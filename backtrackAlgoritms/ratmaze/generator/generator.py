import numpy as np
from random import randint

def generateMaze(n):
	maze = np.array([[randint(0,1) for _ in range(n)] for _ in range(n)])
	maze[0][0], maze[-1][-1] = 1, 1
	return maze


	
