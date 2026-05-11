# [Silver I] 단지번호붙이기 (BOJ 2667)
# 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색, 격자 그래프, 플러드 필
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

from collections import deque

n = int(input())
grid = []
for i in range(n):
    grid.append(list(map(int, input())))

visited = [[False] * n for _ in range(n)]
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and not visited[y][x] and grid[y][x]

def bfs(start_x, start_y):
    q = deque()
    q.append((start_x, start_y))
    visited[start_y][start_x] = True
    count = 1

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = dx + x, dy + y
            if can_go(new_x, new_y):
                visited[new_y][new_x] = True
                count += 1
                q.append((new_x, new_y))
            
    return count

num = []
for i in range(n):
    for j in range(n):
        if can_go(i, j):
            num.append(bfs(i, j))

print(len(num))
for i in sorted(num):
    print(i)
    