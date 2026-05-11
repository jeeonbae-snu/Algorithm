# [Gold II] 집 구하기 (BOJ 13911)
# 분류: 그래프 이론, 최단 경로, 데이크스트라
# 접근: 인접 리스트 기반 그래프 탐색

INF = float('inf')
import heapq
import sys
input = sys.stdin.readline

def dijkstra_multiple(sources):
    d = [INF]*V
    pq = []
    for s in sources:
        d[s] = 0
        heapq.heappush(pq, (0, s))
    while pq:
        dist, u = heapq.heappop(pq)
        if dist > d[u]: continue
        for v, w in graph[u]:
            nd = dist + w
            if nd < d[v]:
                d[v] = nd
                heapq.heappush(pq, (nd, v))
    return d

V, E = map(int, input().split())
adj = [dict() for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    u-=1; v-=1
    if v not in adj[u] or w<adj[u][v]: adj[u][v]=w
    if u not in adj[v] or w<adj[v][u]: adj[v][u]=w

graph = [[] for _ in range(V)]
for u in range(V):
    for v, w in adj[u].items():
        graph[u].append((v, w))

M, x = map(int, input().split())
macs = [int(i)-1 for i in input().split()]
S, y = map(int, input().split())
stars = [int(i)-1 for i in input().split()]

mac_set = set(macs)
star_set = set(stars)

dist_mac = dijkstra_multiple(macs)
dist_star = dijkstra_multiple(stars)

ans = INF
for i in range(V):
    if i in mac_set or i in star_set:
        continue
    if dist_mac[i] <= x and dist_star[i] <= y:
        ans = min(ans, dist_mac[i] + dist_star[i])

print(-1 if ans==INF else ans)
