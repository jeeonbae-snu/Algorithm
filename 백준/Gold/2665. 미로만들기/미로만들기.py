# [Gold IV] 미로만들기 (BOJ 2665)
# 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 최단 경로, 데이크스트라, 격자 그래프, 0-1 너비 우선 탐색
# 접근: 우선순위 큐(heapq)로 시작점에서 각 노드까지의 최단거리 갱신

INF = float('inf')
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

import heapq

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dijkstra(sx, sy, ex, ey):
    costs = [[INF] * n for _ in range(n)]
    costs[sy][sx] = 0
    pq = [(0, sx, sy)]

    while pq:
        curr_cost, x, y = heapq.heappop(pq)

        if curr_cost > costs[y][x]:
            continue

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if in_range(nx, ny):
                new_cost = curr_cost + 1 - board[ny][nx]

                if new_cost < costs[ny][nx]:
                    costs[ny][nx] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny))

    return costs[ey][ex]

n = int(input())
board = [list(map(int, input().strip())) for _ in range(n)]

print(dijkstra(0, 0, n - 1, n - 1))