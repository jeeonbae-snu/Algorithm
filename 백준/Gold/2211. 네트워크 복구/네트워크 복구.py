import sys
import heapq

input = sys.stdin.readline
INF = 10**18

N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

def dijkstra(start: int):
    dist = [INF] * (N + 1)
    parent = [-1] * (N + 1)  # 최단경로 트리에서의 부모(이전 정점)
    dist[start] = 0
    pq = [(0, start)]  # (거리, 정점)

    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v))
    return dist, parent

# 보통 시작점은 1번 컴퓨터
_, parent = dijkstra(1)

edges = []
for v in range(1, N + 1):
    if parent[v] != -1:
        edges.append((parent[v], v))

print(len(edges))
for a, b in edges:
    print(a, b)
