# [Gold III] 별자리 만들기 (BOJ 4386)
# 분류: 그래프 이론, 최소 스패닝 트리
# 접근: 인접 리스트 기반 그래프 탐색

from itertools import combinations

def cal_distance(x, y):
    return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5

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

n = int(input())
stars = []
for i in range(n):
    stars.append(list(map(float, input().split())) + [i])

edges = []
for x, y in combinations(stars, 2):
    edges.append((x[2], y[2], cal_distance(x, y)))
edges.sort(key=lambda x: x[2])
parent = [i for i in range(n)]
size = [1] * n
distance, cnt = 0, 0

for u, v, c in edges:
    if find(u) != find(v):
        union(u, v)
        distance += c
        cnt += 1
        if cnt >= n - 1:
            break

print(f"{distance:.2f}")

