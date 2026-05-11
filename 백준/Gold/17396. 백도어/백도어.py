# [Gold V] 백도어 (BOJ 17396)
# 분류: 그래프 이론, 최단 경로, 데이크스트라
# 접근: 인접 리스트 기반 그래프 탐색

INF = float('inf')

import heapq

def dijkstra(start, end):
    times = [INF] * N
    times[start] = 0
    hq = [(0, start)]

    while hq:
        curr_time, curr_vertex = heapq.heappop(hq)

        if curr_time > times[curr_vertex] or can_see[curr_vertex]:
            continue

        for neighbor, weight in graph[curr_vertex]:
            time = weight + curr_time
            if time < times[neighbor]:
                times[neighbor] = time
                heapq.heappush(hq, (time, neighbor))

    return times[end]

N, M = map(int, input().split())
can_see = list(map(int, input().split())) # 0: 보이지 않음 1: 보임
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

time = dijkstra(0, N - 1)
if time != INF:
    print(time)
else:
    print(-1)
