# [Gold I] 다리 만들기 2 (BOJ 17472)
# 분류: 구현, 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색, 최소 스패닝 트리
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

from collections import deque

def find_bridge(n, lands):
    bridges = []
    INF = float('INF')
    cost = [[INF]*n for _ in range(n)]
    # lands[i] 는 [(x,y), ...] 형태
    for i in range(n):
        for j in range(i+1, n):
            for xi, yi in lands[i]:
                for xj, yj in lands[j]:
                    # 같은 열(세로 다리)
                    if xi == xj:
                        y1, y2 = sorted((yi, yj))
                        length = y2 - y1 - 1
                        if length >= 2:
                            # 중간에 섬(1)이 있는지 검증
                            valid = True
                            for y in range(y1+1, y2):
                                if board[y][xi] == 1:
                                    valid = False
                                    break
                            if valid:
                                cost[i][j] = min(cost[i][j], length)

                    # 같은 행(가로 다리)
                    elif yi == yj:
                        x1, x2 = sorted((xi, xj))
                        length = x2 - x1 - 1
                        if length >= 2:
                            valid = True
                            for x in range(x1+1, x2):
                                if board[yi][x] == 1:
                                    valid = False
                                    break
                            if valid:
                                cost[i][j] = min(cost[i][j], length)

            # 대칭도 같이 채워 주면, 나중에 i<j 만 보는 로직이 깔끔해집니다
            if cost[i][j] < INF:
                cost[j][i] = cost[i][j]

    # cost > 1 (즉, 길이 >= 2)인 것만 모아서 반환
    for i in range(n):
        for j in range(i+1, n):
            if cost[i][j] >= 2:
                bridges.append((i, j, cost[i][j]))
    return bridges

def in_range(x, y):
    return 0 <= x < M and 0 <= y < N

def explore_land(x, y, visited):
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    visited[y][x] = True
    q = deque([(x, y)])
    land = [(x, y)]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[ny][nx] and board[ny][nx]:
                visited[ny][nx] = True
                q.append((nx, ny))
                land.append((nx, ny))
    return land

def find_land(board):
    lands = []
    visited = [[False] * M for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if board[y][x] and not visited[y][x]:
                lands.append(explore_land(x, y, visited))
    return lands

def union(x, y):
    px = find(x)
    py = find(y)

    if px == py:
        return

    if size[px] >= size[py]:
        parent[py] = px
        size[px] += size[py]
    else:
        parent[px] = py
        size[py] += size[px]

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
lands = find_land(board)
n = len(lands)
bridges = find_bridge(n, lands)
bridges.sort(key=lambda x:x[2])
parent = [x for x in range(n)]
size = [1] * n
dist, cnt = 0, 0

for u, v, c in bridges:
    if find(u) != find(v):
        union(u, v)
        dist += c
        cnt += 1
        if cnt >= n - 1:
            break
print(dist) if dist != float("inf") else print(-1)

