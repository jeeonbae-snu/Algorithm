# [Gold IV] 서강그라운드 (BOJ 14938)
# 분류: 그래프 이론, 최단 경로, 데이크스트라, 플로이드–워셜
# 접근: 인접 리스트 기반 그래프 탐색

import heapq

def dijkstra(start):
    INF = float('inf')
    dists = [INF] * n
    dists[start] = 0
    pq = [(0, start)]

    while pq:
        cur_dist, cur_vertex = heapq.heappop(pq)
        if cur_dist > dists[cur_vertex]:
            continue

        for neighbor, weight in graph[cur_vertex]:
            dist = weight + cur_dist
            if dist < dists[neighbor]:
                dists[neighbor] = dist
                heapq.heappush(pq, (dist, neighbor))

    return dists

n, m, r = map(int, input().split())
item = list(map(int, input().split()))
graph = [[] for _ in range(n)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a - 1].append((b - 1, l))
    graph[b - 1].append((a - 1, l))

max_items = 0
for i in range(n):
    dists = dijkstra(i)
    items = 0
    for j in range(n):
        if dists[j] <= m:
            items += item[j]
    max_items = max(max_items, items)

print(max_items)