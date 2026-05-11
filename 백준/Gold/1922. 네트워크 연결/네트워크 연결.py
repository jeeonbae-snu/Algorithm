# [Gold IV] 네트워크 연결 (BOJ 1922)
# 분류: 그래프 이론, 최소 스패닝 트리
# 접근: 인접 리스트 기반 그래프 탐색

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

def union(x, y):
    px, py = find(x), find(y)

    if px == py:
        return False

    if size[px] < size[py]:
        px, py = py, px

    parent[py] = px
    size[px] += size[py]

    return True

N = int(input())
M = int(input())
edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    if a == b:
        continue
    a -= 1
    b -= 1
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])
parent = [i for i in range(N)]
size = [1] * N

min_cost = 0

for u, v, c in edges:
    if find(u) != find(v):
        union(u, v)
        min_cost += c

print(min_cost)

