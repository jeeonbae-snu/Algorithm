INF = float('inf')

import heapq

def dijkstra(start):
    dist = [INF] * n
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

    cnt = 0
    max_dist = 0
    for i in range(n):
        if dist[i] != INF:
            max_dist = max(max_dist, dist[i])
            cnt += 1

    return cnt, max_dist


T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    c -= 1

    graph = [[] for _ in range(n)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        a -= 1
        b -= 1
        # graph[a].append((b, s))
        graph[b].append((a, s))
    cnt, min_time = dijkstra(c)
    print(cnt, min_time)


