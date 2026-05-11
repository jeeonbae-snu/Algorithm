# [Gold IV] 녹색 옷 입은 애가 젤다지? (BOJ 4485)
# 분류: 그래프 이론, 그래프 탐색, 최단 경로, 데이크스트라, 격자 그래프
# 접근: 우선순위 큐(heapq)로 시작점에서 각 노드까지의 최단거리 갱신

INF = float('inf')
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

import heapq

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def dijkstra(sx, sy, ex, ey):
    costs = [[INF] * N for _ in range(N)]
    costs[sy][sx] = board[sy][sx]
    pq = [(board[sy][sx], sx, sy)]

    while pq:
        curr_cost, x, y = heapq.heappop(pq)

        if curr_cost > costs[y][x]:
            continue

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if in_range(nx, ny):
                new_cost = curr_cost + board[ny][nx]

                if new_cost < costs[ny][nx]:
                    costs[ny][nx] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny))

    return costs[ey][ex]

t = 0
while True:
    N = int(input())
    if N == 0:
        break
    t += 1
    board = [list(map(int, input().split())) for _ in range(N)]
    print(f'Problem {t}: {dijkstra(0, 0, N - 1, N - 1)}')

