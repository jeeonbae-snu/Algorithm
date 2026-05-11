# [Silver I] 미로 탐색 (BOJ 2178)
# 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 격자 그래프
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

from collections import deque
n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input())))

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

visited = [[False] * m for _ in range(n)]
distance = [[0] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x < m and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and not visited[y][x] and grid[y][x] == 1

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    distance[0][0] = 1
   
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            if can_go(new_x, new_y):
                distance[new_y][new_x] = distance[y][x] + 1
                visited[new_y][new_x] = True
                q.append((new_x, new_y))

    return distance[n-1][m-1]

print(bfs())