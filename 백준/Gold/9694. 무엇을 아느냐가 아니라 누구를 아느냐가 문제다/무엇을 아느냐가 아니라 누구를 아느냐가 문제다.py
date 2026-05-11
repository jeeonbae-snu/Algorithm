# [Gold III] 무엇을 아느냐가 아니라 누구를 아느냐가 문제다 (BOJ 9694)
# 분류: 그래프 이론, 최단 경로, 데이크스트라, 역추적
# 접근: 인접 리스트 기반 그래프 탐색

import sys
import heapq

INF = float('inf')

def dijkstra(start):
    dist = [INF] * M
    prev = [-1] * M

    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u  # ← 여기서 부모(predecessor)를 기록
                heapq.heappush(pq, (nd, v))
    return dist, prev

T = int(sys.stdin.readline())
for t in range(1, T + 1):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(M)]
    for _ in range(N):
        x, y, z = map(int, sys.stdin.readline().split())
        graph[x].append((y, z))
        graph[y].append((x, z))

    dist, prev = dijkstra(0)
    if dist[M - 1] == INF:
        print(f"Case #{t}: -1")
    else:
        path = []
        cur = M - 1
        while cur != -1:
            path.append(cur)
            cur = prev[cur]
        path.reverse()
        print(f"Case #{t}:", *path)
