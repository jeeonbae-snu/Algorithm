# [Gold V] 택배 배송 (BOJ 5972)
# 분류: 그래프 이론, 최단 경로, 데이크스트라
# 접근: 인접 리스트 기반 그래프 탐색

import heapq

def dijkstar(start):
    distances = [float('inf')] * N
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

    return distances

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u - 1].append((v - 1, w))
    graph[v - 1].append((u - 1, w))

distances = dijkstar(0)
print(distances[N - 1])
