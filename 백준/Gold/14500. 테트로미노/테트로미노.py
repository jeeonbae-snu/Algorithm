# [Gold IV] 테트로미노 (BOJ 14500)
# 분류: 구현, 브루트포스 알고리즘
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

import sys
input = sys.stdin.readline

def dfs(x, y, cnt, total, visited):
    global max_sum
    if cnt == 4:
        max_sum = max(max_sum, total)
        return
    
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N and (nx, ny) not in visited:
            visited.add((nx, ny))
            dfs(nx, ny, cnt + 1, total + paper[ny][nx], visited)
            visited.remove((nx, ny))

def check_t_shape(x, y):
    global max_sum
    for t in t_shapes:
        total = 0
        valid = True
        for dx, dy in t:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < M and 0 <= ny < N):
                valid = False
                break
            total += paper[ny][nx]
        if valid:
            max_sum = max(max_sum, total)

N, M = map(int, input().split())
paper = [[int(x) for x in input().split()] for _ in range(N)]
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
t_shapes = [
    [(0, 0), (0, -1), (0, 1), (-1, 0)],
    [(0, 0), (0, -1), (0, 1), (1, 0)],
    [(0, 0), (-1, 0), (1, 0), (0, -1)],
    [(0, 0), (-1, 0), (1, 0), (0, 1)]
]
max_sum = 0

for y in range(N):
    for x in range(M):
        visited = {(x, y)}
        dfs(x, y, 1, paper[y][x], visited)
        check_t_shape(x, y)

print(max_sum)