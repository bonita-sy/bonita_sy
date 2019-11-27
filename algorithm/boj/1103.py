n, m = map(int, input().split(" "))
board_state = [list(input())  for _ in range(n)]
visited_board = [[False] * m   for _ in range(n)]
count_board = [[-1] * m   for _ in range(n)]

#top, bottom, left, right
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

x, y= [0, 0]

def move(x, y):
	if (x > n-1 or x < 0) or (y > m-1 or y < 0) or board_state[x][y] == 'H':
		return 0

	if visited_board[x][y]:
		return -1

	if count_board[x][y] != -1:
		return count_board[x][y]

	visited_board[x][y] = True

	for i in range(4):
		distance = int(board_state[x][y])
		nx = x + dx[i] * distance
		ny = y + dy[i] * distance
		count_board[x][y] = max(count_board[x][y], move(nx, ny)+1)

	visited_board[x][y] = False
	return count_board[x][y]
		
	


if __name__=="__main__":
	print(move(0, 0))
