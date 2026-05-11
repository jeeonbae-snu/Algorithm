# [Gold III] 피리 부는 사나이 (BOJ 16724)
# 분류: 그래프 이론, 자료 구조, 그래프 탐색, 깊이 우선 탐색, 분리 집합, 격자 그래프
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

from collections import deque

def bfs(sx, sy):
    visited[sy][sx] = True
    q = deque([(sx, sy)])

    while q:
        x, y = q.popleft()
        dx, dy = directions[board[y][x]]
        nx, ny = x + dx, y + dy

        if not visited[ny][nx]:
            q.append((nx, ny))
            visited[ny][nx] = True

        for px, py in rev[y][x]:
            if not visited[py][px]:
                visited[py][px] = True
                q.append((px, py))

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
directions = {'D':(0, 1), 'U':(0, -1), 'L':(-1, 0), 'R':(1, 0)}

rev = [[[] for _ in range(M)] for _ in range(N)]
for y in range(N):
    for x in range(M):
        dx, dy = directions[board[y][x]]
        rev[y + dy][x + dx].append((x, y))

visited = [[False] * M for _ in range(N)]
cnt = 0
for y in range(N):
    for x in range(M):
        if not visited[y][x]:
            bfs(x, y)
            cnt += 1
print(cnt)