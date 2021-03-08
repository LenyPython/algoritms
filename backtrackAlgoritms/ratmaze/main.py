

testmaze = [[1,1,1,0],
			[1,0,1,0],
			[1,0,1,0],
			[1,0,0,1]]

n = len(testmaze) - 1

def backtrack(maze, i, j, n):
	if i == n and j == n: return True

	if i <= n and j <= n:
		if maze[i][j]:
			return True if backtrack(maze, i + 1, j, n) or backtrack(maze, i, j + 1, n) else False

def main():
	print(backtrack(testmaze, 0, 0, n))


if __name__ == '__main__':
	main()

