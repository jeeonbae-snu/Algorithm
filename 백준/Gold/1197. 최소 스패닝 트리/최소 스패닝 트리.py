# [Gold IV] 최소 스패닝 트리 (BOJ 1197)
# 분류: 최소 스패닝 트리, 그래프 이론
# 접근: 인접 리스트 기반 그래프 탐색

def union(x, y):
    px = find(x)
    py = find(y)

    if px == py:
        return

    if size[px] > size[py]:
        parent[py] = px
        size[px] += size[py]
    else:
        parent[px] = py
        size[py] += size[px]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

V, E = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(E)]

edges.sort(key=lambda x: x[2])
parent = [x for x in range(V + 1)]
size = [1] * (V + 1)
distance, cnt = 0, 0

for u, v, c in edges:
    if find(u) != find(v):
        union(u, v)
        distance += c
        cnt += 1

        if cnt >= V - 1:
            break

print(distance)