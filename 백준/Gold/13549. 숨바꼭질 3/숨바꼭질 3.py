# [Gold V] 숨바꼭질 3 (BOJ 13549)
# 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 최단 경로, 데이크스트라, 0-1 너비 우선 탐색
# 접근: 우선순위 큐(heapq)로 시작점에서 각 노드까지의 최단거리 갱신

import heapq

def dijkstra(start, end):
    INF = float('inf')
    MAX_K = 100001
    times = [INF] * MAX_K
    times[start] = 0
    hq = [(0, start)]

    while hq:
        curr_time, curr_loc = heapq.heappop(hq)

        if curr_time > times[curr_loc]:
            continue

        if curr_loc == end:
            return curr_time

        for next_loc, cost in ((curr_loc - 1, 1),
                               (curr_loc + 1, 1),
                               (curr_loc * 2, 0)):
            if 0 <= next_loc < MAX_K:
                new_time = curr_time + cost
                if new_time < times[next_loc]:
                    times[next_loc] = new_time
                    heapq.heappush(hq, (new_time, next_loc))

    return - 1

N, K = map(int, input().split())
print(dijkstra(N, K))
