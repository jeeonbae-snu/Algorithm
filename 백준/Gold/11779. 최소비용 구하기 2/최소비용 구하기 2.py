# [Gold III] 최소비용 구하기 2 (BOJ 11779)
# 분류: 그래프 이론, 최단 경로, 데이크스트라, 역추적
# 접근: 인접 리스트 기반 그래프 탐색

import sys
import heapq
from typing import List, Tuple

def dijkstra(start: int, end: int, n: int, cost: List[List[int]]) -> Tuple[int, List[int]]:
    """
    Compute the minimum cost and record the path from `start` to `end` using Dijkstra's algorithm.

    :return: A tuple of (min_cost, parent_list)
             where parent_list[v] is the previous node on the shortest path to v.
    """
    INF = float('inf')
    dist = [INF] * n
    parent = [-1] * n
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        cur_cost, u = heapq.heappop(heap)
        if cur_cost > dist[u]:
            continue
        if u == end:
            break
        for v in range(n):
            if cost[u][v] != -1:
                new_cost = cur_cost + cost[u][v]
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    parent[v] = u
                    heapq.heappush(heap, (new_cost, v))
    return dist[end], parent

def reconstruct_path(start: int, end: int, parent: List[int]) -> List[int]:
    """
    Reconstruct the path from start to end using the parent list.
    Returns the path as a list of 1-based node indices.
    """
    path = []
    curr = end
    while curr != -1:
        path.append(curr + 1)
        if curr == start:
            break
        curr = parent[curr]
    return path[::-1]

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    m = int(input().strip())

    cost = [[-1] * n for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        if cost[u][v] == -1 or w < cost[u][v]:
            cost[u][v] = w

    start, end = map(int, input().split())
    start -= 1
    end -= 1

    min_cost, parent = dijkstra(start, end, n, cost)
    if min_cost == float('inf'):
        print(-1)
        return

    print(min_cost)
    path = reconstruct_path(start, end, parent)
    print(len(path))
    print(*path)

if __name__ == '__main__':
    main()
