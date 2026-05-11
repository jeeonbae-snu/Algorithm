# [Gold V] 적록색약 (BOJ 10026)
# 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색, 격자 그래프
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

from collections import deque

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def bfs(sx, sy, v, blindness):
    q = deque()
    color = board[sy][sx]
    v[sy][sx] = True
    q.append((sx, sy))

    while q:
        x, y = q.popleft()

        for dx, dy in zip([1, 0, -1, 0], [0, 1, 0, -1]):
            nx, ny = x + dx, y + dy

            if not blindness:
                if in_range(nx, ny) and not visited[ny][nx] and color == board[ny][nx]:
                    q.append((nx, ny))
                    v[ny][nx] = True

            else:
                if color == 'R' or color == 'G':
                    if in_range(nx, ny) and not v[ny][nx] and (board[ny][nx] == 'R' or board[ny][nx] == 'G'):
                        q.append((nx, ny))
                        v[ny][nx] = True
                else:
                    if in_range(nx, ny) and not v[ny][nx] and color == board[ny][nx]:
                        q.append((nx, ny))
                        v[ny][nx] = True

    return v

N = int(input())
board = [list(input().strip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
visited_blindness = [[False] * N for _ in range(N)]
cnt = 0
cnt_blindness = 0

for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            visited = bfs(x, y, visited, False)
            cnt += 1

for y in range(N):
    for x in range(N):
        if not visited_blindness[y][x]:
            visited_blindness = bfs(x, y, visited_blindness, True)
            cnt_blindness += 1

print(cnt, cnt_blindness)

