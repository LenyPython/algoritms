

def findPaths(maze, pos_x, pos_y, size, paths = [], way = []):
	if pos_x == pos_y == size: paths.append(way)

