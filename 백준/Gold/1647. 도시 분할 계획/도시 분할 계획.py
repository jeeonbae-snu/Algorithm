# [Gold IV] 도시 분할 계획 (BOJ 1647)
# 분류: 그래프 이론, 최소 스패닝 트리
# 접근: 인접 리스트 기반 그래프 탐색

import sys
input = sys.stdin.readline
INF = float('inf')

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        return

    if rank[root_x] > rank[root_y]:
        parents[root_y] = root_x
    elif rank[root_y] > rank[root_x]:
        parents[root_x] = root_y
    else:
        parents[root_y] = root_x
        rank[root_x] += 1

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])

    return parents[x]

N, M = map(int, input().split())
edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a - 1, b - 1, c))

edges.sort(key=lambda x: x[2])

total_cost = 0
max_edge = 0
parents = [i for i in range(N)]
rank = [0] * N

for u, v, w in edges:
    if find(u) != find(v):
        union(u, v)
        total_cost += w
        max_edge = max(max_edge, w)

print(total_cost - max_edge)