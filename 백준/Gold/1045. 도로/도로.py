import sys

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
    return True

input = sys.stdin.readline

N, M = map(int, input().split())

# 간선 수집
edges = []
rows = []
for i in range(N):
    row = list(input().strip())  # 공백 없이 'Y'/'N'
    rows.append(row)

for i in range(N):
    for j in range(i + 1, N):
        if rows[i][j] == 'Y':
            edges.append((i, j))

# 사전식 오름차순 정렬(=우선순위 높은 것부터)
edges.sort()

E = len(edges)
# M개를 고르려면 전체 간선이 M개 이상이어야 함
if M > E:
    print(-1)
    sys.exit(0)

# 전체 그래프가 애초에 연결 가능한지 확인
parent = list(range(N))
size = [1] * N
for u, v in edges:
    union(u, v)
root = find(0) if N > 0 else 0
if any(find(x) != root for x in range(N)):
    print(-1)
    sys.exit(0)

# 사전식으로 가장 앞선 스패닝 트리 구성
parent = list(range(N))
size = [1] * N
tree = []
for u, v in edges:
    if union(u, v):
        tree.append((u, v))
        if len(tree) == max(0, N - 1):
            break

if len(tree) < max(0, N - 1):
    print(-1)
    sys.exit(0)

# M개가 될 때까지 남은 간선 앞에서 채우기
picked = set(tree)
ans = list(tree)
for e in edges:
    if len(ans) == M:
        break
    if e not in picked:
        ans.append(e)
        picked.add(e)

if len(ans) < M:
    print(-1)
    sys.exit(0)

# 차수 계산 후 출력
deg = [0] * N
for u, v in ans:
    deg[u] += 1
    deg[v] += 1

print(*deg)
