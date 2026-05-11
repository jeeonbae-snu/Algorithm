# [Gold IV] 타임머신 (BOJ 11657)
# 분류: 그래프 이론, 최단 경로, 벨만–포드
# 접근: 인접 리스트 기반 그래프 탐색

def bellman(start):
    times = [float('inf')] * N
    times[start] = 0

    for _ in range(N - 1):
        for u in range(N):
            for v, weight in graph[u]:
                if times[u] != float('inf') and times[u] + weight < times[v]:
                    times[v] = times[u] + weight

    for u in range(N):
        for v, weight in graph[u]:
            if times[u] != float('inf') and times[u] + weight < times[v]:
                return -1

    return times[1:]

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u - 1].append((v - 1, w))

result = bellman(0)
if result == -1:
    print(result)
else:
    for t in result:
        if t == float('INF'):
            print(-1)
        else:
            print(t)
