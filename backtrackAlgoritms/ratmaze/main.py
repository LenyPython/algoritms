from generator.generator import generateMaze


def backtrack(maze, i, j, n):
	if i == n and j == n: return True

	if i <= n and j <= n:
		if maze[i][j]:
			return True if backtrack(maze, i + 1, j, n) or backtrack(maze, i, j + 1, n) else False

def main():
	n = ''
	while not n.isdigit():
		n = input('Choose a maze size (n x n): ')
	n = int(n)
	arrLen = n - 1
	mainMaze = generateMaze(n)
	print(mainMaze)
	print(f'Has a solution: {backtrack(mainMaze, 0, 0, arrLen)}')
	while not backtrack(mainMaze, 0, 0, arrLen):
		mainMaze =generateMaze(n)
		print(mainMaze)
		print(f'Has a solution: {backtrack(mainMaze, 0, 0, arrLen)}')


if __name__ == '__main__':
	main()

