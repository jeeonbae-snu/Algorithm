# [Gold IV] 알고스팟 (BOJ 1261)
# 분류: 그래프 이론, 그래프 탐색, 최단 경로, 데이크스트라, 격자 그래프, 0-1 너비 우선 탐색
# 접근: 우선순위 큐(heapq)로 시작점에서 각 노드까지의 최단거리 갱신

import heapq

INF = float('inf')
dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def dijkstra(sx, sy, ex, ey):
    costs = [[INF] * N for _ in range(M)]
    costs[sy][sx] = 0
    pq = [(0, sx, sy)]

    while pq:
        curr_cost, x, y = heapq.heappop(pq)

        if curr_cost > costs[y][x]:
            continue

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            cost = board[y][x] + curr_cost
            if in_range(nx, ny) and cost < costs[ny][nx]:
                costs[ny][nx] = cost
                heapq.heappush(pq, (cost, nx, ny))

    return costs[ey][ex]

N, M = map(int, input().split()) # N: 가로, M: 세로
board = [list(map(int, input().strip())) for _ in range(M)]
print(dijkstra(0, 0, N - 1, M - 1))