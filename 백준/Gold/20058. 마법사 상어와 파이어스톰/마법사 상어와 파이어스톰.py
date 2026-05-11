# [Gold III] 마법사 상어와 파이어스톰 (BOJ 20058)
# 분류: 구현, 그래프 이론, 그래프 탐색, 시뮬레이션, 너비 우선 탐색, 깊이 우선 탐색
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

from collections import deque

def rotate_matrix(mat, sz):
    new_mat = [[0] * sz for _ in range(sz)]
    for i in range(sz):
        for j in range(sz):
            new_mat[i][j] = mat[sz - j - 1][i]
    return new_mat

def melt_ice():
    melt_list = []
    for y in range(grid_size):
        for x in range(grid_size):
            if grid[y][x] <= 0:
                continue
            cnt = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < grid_size and 0 <= ny < grid_size and grid[ny][nx] > 0:
                    cnt += 1
            if cnt < 3:
                melt_list.append((x, y))
    for x, y in melt_list:
        grid[y][x] -= 1

def bfs_count(sx, sy):
    q = deque()
    q.append((sx, sy))
    visited[sy][sx] = True
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size and not visited[ny][nx] and grid[ny][nx] > 0:
                visited[ny][nx] = True
                q.append((nx, ny))
                cnt += 1
    return cnt

N, Q = map(int, input().split())
grid_size = 2**N
grid = [list(map(int, input().split())) for _ in range(grid_size)]
operations = list(map(int, input().split()))
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for op in operations:
    step = 2**op
    for y in range(0, grid_size, step):
        for x in range(0, grid_size, step):
            subgrid = [row[x:x+step] for row in grid[y:y+step]]
            rotated = rotate_matrix(subgrid, step)
            for dy in range(step):
                grid[y+dy][x:x+step] = rotated[dy]
    melt_ice()

total_ice = sum(sum(row) for row in grid)
visited = [[False] * grid_size for _ in range(grid_size)]
max_region = 0
for y in range(grid_size):
    for x in range(grid_size):
        if grid[y][x] > 0 and not visited[y][x]:
            max_region = max(max_region, bfs_count(x, y))
print(total_ice)
print(max_region)
