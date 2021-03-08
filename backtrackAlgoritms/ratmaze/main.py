

testmaze = [[1,1,1,0],
			[1,0,1,0],
			[1,0,1,0],
			[1,0,1,1]]

n = len(testmaze) - 1

def backtrack(maze, i, j, n, step):
	step += 1
	print([i, j], step)
	if i == n and j == n:
		print('True')
		return True
	if i <= n and j <= n:
		if maze[i][j]:
			backtrack(maze, i + 1, j, n, step)
			backtrack(maze, i, j + 1, n, step)
	return False

def main():
	for r in testmaze:
		print(r)
	print(backtrack(testmaze, 0, 0, n, 0))


if __name__ == '__main__':
	main()

