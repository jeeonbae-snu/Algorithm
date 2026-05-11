import heapq
import sys

input = sys.stdin.readline
INF = float('inf')

def dijkstra(start):
    dists = [INF] * N
    dists[start] = 0
    pq = [(0, start)]
    while pq:
        cur_dist, u = heapq.heappop(pq)
        if cur_dist > dists[u]:
            continue
        for v, w in graph[u]:
            nd = cur_dist + w
            if nd < dists[v]:
                dists[v] = nd
                heapq.heappush(pq, (nd, v))
    return dists

N, M, X, Y = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 1) 최단 거리 계산
dists = dijkstra(Y)

# 2) 도달 불가 확인
if any(d == INF for i, d in enumerate(dists) if i != Y):
    print(-1)
    sys.exit()

# 3) 왕복 거리 리스트 생성 및 정렬
round_trips = sorted(2 * dists[i] for i in range(N) if i != Y)

# 4) 하루 예산 X로 며칠 걸리는지 계산
days = 1
rem = X
for r in round_trips:
    if r > X:
        print(-1)
        sys.exit()
    if r <= rem:
        rem -= r
    else:
        days += 1
        rem = X - r

print(days)