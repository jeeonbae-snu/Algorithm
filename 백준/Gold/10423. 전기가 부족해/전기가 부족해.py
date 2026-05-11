# 발전소 여러 개가 있을 때 최소 비용으로 모든 도시를 전력망에 연결
# (발전소들은 처음부터 같은 컴포넌트로 취급)

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

N, M, K = map(int, input().split())
P = [int(x) - 1 for x in input().split()]  # 발전소 번호(0-index)

edges = []
for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((w, u-1, v-1))  # 가중치 먼저 두면 정렬 편함

edges.sort()  # w 오름차순

parent = list(range(N))
size = [1]*N

# 발전소들을 하나의 컴포넌트로 미리 합치기
for i in range(1, K):
    union(P[0], P[i])

min_cost = 0
for w, u, v in edges:
    if union(u, v):
        min_cost += w

print(min_cost)
