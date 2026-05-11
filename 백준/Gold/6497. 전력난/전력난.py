# [Gold IV] 전력난 (BOJ 6497)
# 분류: 그래프 이론, 최소 스패닝 트리
# 접근: 인접 리스트 기반 그래프 탐색

import sys
input = sys.stdin.readline

def union(x,y):
    px = find(x)
    py = find(y)

    if px == py:
        return

    if size[px] > size[py]:
        parent[py] = px
    elif size[px] < size[py]:
        parent[px] = py
    else:
        parent[py] = px
        size[px] += 1

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

while True:
    m, n = map(int, input().split())
    if (m, n) == (0, 0):
        break

    edges = [list(map(int, input().split())) for _ in range(n)]
    total_dist = sum(x[2] for x in edges)

    edges.sort(key=lambda x:x[2])
    parent = [x for x in range(m)]
    size = [1] * n
    distance, cnt = 0, 0

    for u, v, c in edges:
        if find(u) != find(v):
            union(u, v)
            distance += c
            cnt += 1
            if cnt >= n - 1:
                break
    print(total_dist - distance)
