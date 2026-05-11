# [Gold IV] 최단경로 (BOJ 1753)
# 분류: 그래프 이론, 최단 경로, 데이크스트라
# 접근: 인접 리스트 기반 그래프 탐색

import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    distances = [float('INF')] * V
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

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u-1].append((v-1, w))

for d in dijkstra(K-1):
    print(d if d != float('inf') else "INF")
