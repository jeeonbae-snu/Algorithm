# [Gold III] 소수마을 (BOJ 14431)
# 분류: 수학, 그래프 이론, 정수론, 집합과 맵, 최단 경로, 데이크스트라, 소수 판정, 에라토스테네스의 체
# 접근: 인접 리스트 기반 그래프 탐색

import heapq
import math
from itertools import combinations
INF = float('inf')
MAX_DIST = 10000

def find_prime_numbers():
    is_prime = [True] * MAX_DIST
    for i in range(2, int(MAX_DIST ** 0.5) + 1):
        if is_prime[i]:
            for j in range(2 * i, MAX_DIST, i):
                is_prime[j] = False

    return [i for i in range(2, MAX_DIST) if is_prime[i]]

def dijkstra(start, end):
    dist = [INF] * (N+2)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        curr_dist, curr_vertex = heapq.heappop(pq)

        if curr_dist > dist[curr_vertex]:
            continue

        for next_vertex, weight in graph[curr_vertex]:
            new_dist = curr_dist + weight
            if new_dist < dist[next_vertex]:
                dist[next_vertex] = new_dist
                heapq.heappush(pq, (new_dist, next_vertex))

    return dist[end]

x1, y1, x2, y2 = map(int, input().split())
N = int(input())
loc = [[i] + list(map(int, input().split())) for i in range(1, N+1)]
loc.append([0, x1, y1])
loc.append([N+1, x2, y2])

graph = [[] for _ in range(N+2)]
prime_numbers = find_prime_numbers()

for loc1, loc2 in combinations(loc, 2):
    id1, x1, y1 = loc1
    id2, x2, y2 = loc2
    dist = int(math.sqrt((x1 - x2)**2 + (y1 - y2)**2))
    if dist in prime_numbers:
        graph[id1].append((id2, dist))
        graph[id2].append((id1, dist))
min_dist = dijkstra(0, N+1)
if min_dist != INF:
    print(min_dist)
else:
    print(-1)