from collections import deque

# 방향: 오른쪽, 아래, 왼쪽, 위 (시계 방향)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 입력
n = int(input())
k = int(input())
board = [[0] * n for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1  # 사과 위치 (1-based → 0-based)

l = int(input())
directions = dict()
for _ in range(l):
    x, c = input().split()
    directions[int(x)] = c

snake = deque()
snake.append((0, 0))  # 초기 위치
time = 0
direction = 0  # 처음엔 오른쪽

x, y = 0, 0

while True:
    time += 1
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 벽에 부딪히는 경우
    if nx < 0 or ny < 0 or nx >= n or ny >= n:
        break

    # 자기 자신과 부딪히는 경우
    if (nx, ny) in snake:
        break

    # 이동
    snake.appendleft((nx, ny))
    if board[nx][ny] == 1:  # 사과가 있다면
        board[nx][ny] = 0  # 사과 먹음
    else:  # 사과가 없으면
        snake.pop()  # 꼬리 이동

    # 방향 전환
    if time in directions:
        if directions[time] == 'L':
            direction = (direction - 1) % 4
        else:  # 'D'
            direction = (direction + 1) % 4

    x, y = nx, ny

print(time)
