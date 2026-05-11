import sys
import heapq

input = sys.stdin.readline
INF = 10**18

def dijkstra(starts):
    dist = [INF] * N
    pq = []
    for s in starts:
        dist[s] = 0
        heapq.heappush(pq, (0, s))
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in rev_graph[u]:  # 역간선 사용
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist

# 입력: N도시, M도로, K시작점(면접장 등)
N, M, K = map(int, input().split())
rev_graph = [[] for _ in range(N)]  # 역간선 그래프

for _ in range(M):
    u, v, c = map(int, input().split())
    u -= 1; v -= 1
    # 도로가 u -> v 라면, 역그래프엔 v -> u 로 저장
    rev_graph[v].append((u, c))

city_num = list(map(int, input().split()))
starts = [x - 1 for x in city_num]  # 1-based -> 0-based

dist = dijkstra(starts)

# 최장거리 도시 찾기 (동률이면 번호 작은 도시)
best_city = 0
best_dist = dist[0]
for i in range(1, N):
    if dist[i] > best_dist or (dist[i] == best_dist and i < best_city):
        best_city = i
        best_dist = dist[i]

print(best_city + 1)  # 도시 번호는 1-based로 출력
print(best_dist)
