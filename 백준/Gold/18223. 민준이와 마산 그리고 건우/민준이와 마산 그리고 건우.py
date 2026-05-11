import heapq
import sys

input = sys.stdin.readline

def dijkstra(start):
    INF = float('inf')
    dists = [INF] * V
    dists[start] = 0
    pq = [(0, start)]
    
    while pq:
        cur_dist, cur_vertex = heapq.heappop(pq)
        if cur_dist > dists[cur_vertex]:
            continue

        for neighbor, weight in graph[cur_vertex]:
            dist = cur_dist + weight
            if dist < dists[neighbor]:
                dists[neighbor] = dist
                heapq.heappush(pq, (dist, neighbor))

    return dists

if __name__ == "__main__":
    V, E, P = map(int, input().split())
    graph = [[] for _ in range(V)]

    for _ in range(E):
        a, b, c = map(int, input().split())
        a -= 1; b -= 1
        graph[a].append((b, c))
        graph[b].append((a, c))

    # 1 → N 최단 거리
    dist_start = dijkstra(0)
    # P → N 최단 거리 (P가 출발점인 경우)
    dist_p = dijkstra(P - 1)

    direct = dist_start[V - 1]                 # 직접 1→N
    via_p = dist_start[P - 1] + dist_p[V - 1]  # 1→P + P→N

    if direct == via_p:
        print("SAVE HIM")
    else:
        print("GOOD BYE")
