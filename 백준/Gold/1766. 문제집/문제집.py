# [Gold II] 문제집 (BOJ 1766)
# 분류: 그래프 이론, 자료 구조, 우선순위 큐, 방향 비순환 그래프, 위상 정렬
# 접근: 인접 리스트 기반 그래프 탐색

import heapq

def topology_sort():
    pq = []
    result = []

    for i in range(N):
        if indegree[i] == 0:
            heapq.heappush(pq, i)

    while pq:
        curr_v = heapq.heappop(pq)
        result.append(curr_v + 1)

        for next_v in graph[curr_v]:
            indegree[next_v] -= 1
            if indegree[next_v] == 0:
                heapq.heappush(pq, next_v)

    return result

N, M = map(int, input().split())
graph = {i: [] for i in range(N)}
indegree = [0] * N

for _ in range(M):
    start, end = map(int, input().split())
    graph[start - 1].append(end - 1)
    indegree[end - 1] += 1

result = topology_sort()

if len(result) == N:
    print(*result)