import sys
import heapq

input = sys.stdin.readline
INF = 10**18

def dijkstra(start, graph):
    n = len(graph) - 1
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist

T = int(input().strip())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        w = d * 2
        # g-h 간선만 홀수(= 2d-1)로 만들어 표시
        if (a == g and b == h) or (a == h and b == g):
            w -= 1
        graph[a].append((b, w))
        graph[b].append((a, w))

    candidates = [int(input()) for _ in range(t)]
    candidates.sort()

    distS = dijkstra(s, graph)

    ans = []
    for x in candidates:
        # 최단거리가 홀수면 g-h를 지나는 최단경로가 존재
        if distS[x] % 2 == 1:
            ans.append(x)

    print(*ans)
