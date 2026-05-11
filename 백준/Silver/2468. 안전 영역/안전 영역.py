# [Silver I] 안전 영역 (BOJ 2468)
# 분류: 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색, 격자 그래프
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

from collections import deque

n = int(input())
grid = [[int(x) for x in input().split()] for _ in range(n)]
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, k, visited):
    return in_range(x, y) and not visited[y][x] and grid[y][x] > k

def bfs(start_x, start_y, k, visited):
    q = deque()
    q.append((start_x, start_y))
    visited[start_y][start_x] = True

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = dx + x, dy + y
            if can_go(new_x, new_y, k, visited):
                visited[new_y][new_x] = True
                q.append((new_x, new_y))
            
    return 1

max_height = max(map(max, grid))
max_count = 1

for k in range(1, max_height):
    count = 0
    visited = [[False] * n for _ in range(n)]  # 매번 visited 배열을 초기화
    for i in range(n):
        for j in range(n):
            if can_go(i, j, k, visited):
                count += bfs(i, j, k, visited)
    max_count = max(count, max_count) 

print(max_count)
