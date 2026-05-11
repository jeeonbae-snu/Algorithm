# [Gold IV] 특정한 최단 경로 (BOJ 1504)
# 분류: 그래프 이론, 최단 경로, 데이크스트라
# 접근: 인접 리스트 기반 그래프 탐색

import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    distances = [float('INF')] * N
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        curr_distance, curr_vertex = heapq.heappop(heap)
        if curr_distance > distances[curr_vertex]:
            continue

        for neighbor, weight in graph[curr_vertex]:
            distance = curr_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

N, E = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u-1].append((v-1, w))
    graph[v-1].append((u-1, w))
v1, v2 = map(int, input().split())
x = dijkstra(0)
y = dijkstra(v1-1)
z = dijkstra(v2-1)
ans = min(x[v1-1] + y[v2-1] + z[N-1], x[v2-1] + z[v1-1] + y[N-1])

if ans > 1e9:
    print(-1)
else:
    print(ans)