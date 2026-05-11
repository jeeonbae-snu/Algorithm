# [Gold II] 빵집 (BOJ 3109)
# 분류: 그래프 이론, 그리디 알고리즘, 그래프 탐색, 깊이 우선 탐색
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

def in_range(x, y):
    return 0 <= x < C and 0 <= y < R

def dfs(x, y, visited):
    visited[y][x] = True

    if x == C - 1:
        return True

    for dx, dy in zip([1, 1, 1], [-1, 0, 1]):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and not visited[ny][nx] and board[ny][nx] != 'x':
            if dfs(nx, ny, visited):
                return True

    return False

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
cnt = 0

for y in range(R):
    if board[y][0] != 'x' and not visited[y][0]:
        if dfs(0, y, visited):
            cnt += 1

print(cnt)

