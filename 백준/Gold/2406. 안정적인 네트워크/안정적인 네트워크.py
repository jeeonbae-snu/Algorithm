import sys

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    pa, pb = find(a), find(b)
    if pa == pb:
        return False
    # union by size
    if size[pa] < size[pb]:
        pa, pb = pb, pa
    parent[pb] = pa
    size[pa] += size[pb]
    return True

input = sys.stdin.readline

n, m = map(int, input().split())

# 지사 간 기존 연결 여부 저장 (1번은 본사라 제외)
connected = [[False]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    connected[x][y] = connected[y][x] = True

# 전체 인접 행렬 (1..n)
adj = [list(map(int, input().split())) for _ in range(n)]

# {2..n}에 대해 간선 리스트 구성
# 이미 연결된 간선은 비용 0, 나머지는 adj 비용
edges = []
for i in range(2, n+1):
    for j in range(i+1, n+1):
        w = 0 if connected[i][j] else adj[i-1][j-1]
        edges.append((w, i, j))

# 크루스칼: 정점 2..n
parent = list(range(n+1))
size = [1]*(n+1)
edges.sort()

total_cost = 0
added = []

# {2..n}에 대해 (n-2)개의 간선이 선택되면 연결
need = (n-1) - 1 if n >= 2 else 0  # {2..n}의 정점 수 = n-1
picked = 0

for w, u, v in edges:
    if union(u, v):
        picked += 1
        if w > 0:
            total_cost += w
            added.append((u, v))
        if picked == need:
            break

# 출력
print(total_cost, len(added))
for u, v in added:
    print(u, v)
