# [Gold V] 간선 이어가기 2 (BOJ 14284)
# 분류: 그래프 이론, 최단 경로, 데이크스트라
# 접근: 인접 리스트 기반 그래프 탐색

import heapq

def dijkstra(start, end):
    INF = float('inf')
    distances = [INF] * n
    distances[start] = 0
    hq = [(0, start)]

    while hq:
        curr_distance, curr_vertex = heapq.heappop(hq)

        if curr_distance > distances[curr_vertex]:
            continue

        for neighbor, weight in graph[curr_vertex]:
            distance = weight + curr_distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(hq, (distance, neighbor))

    return distances[end]

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u - 1].append((v - 1, w))
    graph[v - 1].append((u - 1, w))

s, t = map(int, input().split())
print(dijkstra(s - 1, t - 1))