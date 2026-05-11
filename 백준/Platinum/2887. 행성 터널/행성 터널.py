import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    a = find(a); b = find(b)
    if a == b:
        return False
    if size[a] < size[b]:
        a, b = b, a
    parent[b] = a
    size[a] += size[b]
    return True

N = int(input())
pts = []
for i in range(N):
    x, y, z = map(int, input().split())
    pts.append((x, y, z, i))

edges = []

# 각 축에서 인접한 쌍만 간선 추가 (가중치는 그 축의 차이)
for axis in range(3):
    pts.sort(key=lambda p: p[axis])
    for i in range(N - 1):
        u = pts[i][3]
        v = pts[i + 1][3]
        w = abs(pts[i][axis] - pts[i + 1][axis])
        edges.append((w, u, v))

# 가중치 기준 정렬
edges.sort()

parent = list(range(N))
size = [1] * N

cost = 0
picked = 0
for w, u, v in edges:
    if union(u, v):
        cost += w
        picked += 1
        if picked == N - 1:
            break

print(cost)
