import sys
input = sys.stdin.readline

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return False
    if size[a] < size[b]:
        a, b = b, a
    parent[b] = a
    size[a] += size[b]
    return True

N, M = map(int, input().split())   # 정점: 0..N (총 N+1개)
edges = []
for _ in range(M + 1):              # ★ M+1개 읽기
    u, v, w = map(int, input().split())
    edges.append((u, v, w))         # ★ 인덱스 보정 없음 (0..N)

def kruskal(count_uphill_first: bool) -> int:
    # count_uphill_first == True  => 오름차순(오르막=0 먼저) → '최악'
    # count_uphill_first == False => 내림차순(내리막=1 먼저) → '최선'
    es = sorted(edges, key=lambda x: x[2], reverse=not count_uphill_first)

    global parent, size
    parent = list(range(N + 1))
    size = [1] * (N + 1)

    picked = 0
    uphill_cnt = 0
    for u, v, w in es:
        if union(u, v):
            picked += 1
            # 원문 정의: 오르막=0
            if w == 0:
                uphill_cnt += 1
            if picked == N:         # 정점 N+1개 → 간선 N개 고르면 완료
                break
    return uphill_cnt ** 2

worst = kruskal(count_uphill_first=True)   # 오름차순: 오르막 최대로 뽑힘
best  = kruskal(count_uphill_first=False)  # 내림차순: 오르막 최소로 뽑힘
print(worst - best)
