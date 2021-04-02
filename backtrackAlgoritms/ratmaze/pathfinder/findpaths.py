

def find_paths(maze, size, pos_x = 0, pos_y = 0, came_from=None, paths = [], way = []):
	if pos_x == pos_y == size:
		way.append([pos_x, pos_y])
		paths.append(way[:])
		way.pop()
	elif pos_x <= size and pos_y <= size:
		if maze[pos_x][pos_y]:
			way.append([pos_x, pos_y])
			if came_from != 'down':
				find_paths(maze, size, pos_x + 1, pos_y, 'top', paths, way)
			if came_from != 'right':
				find_paths(maze, size, pos_x, pos_y + 1, 'left', paths, way)
			if came_from != 'top':
				if pos_x > 0 and pos_y > 1:
					if not maze[pos_x - 1][pos_y - 1]:
						find_paths(maze, size, pos_x - 1, pos_y, 'down', paths, way)
			if came_from != 'left':
				if pos_x > 1 and pos_y > 0:
					if not maze[pos_x - 1][pos_y - 1] or not maze[pos_x][pos_y - 1]:
						find_paths(maze, size, pos_x, pos_y - 1, 'right', paths, way)
			way.pop()
			return paths

