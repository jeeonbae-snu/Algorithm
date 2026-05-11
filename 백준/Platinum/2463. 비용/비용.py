import sys

MOD = 10**9

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)
N = next(it); M = next(it)

edges = [(next(it), next(it), next(it)) for _ in range(M)]
# 가중치 내림차순
edges.sort(key=lambda e: e[2], reverse=True)

# ----- DSU -----
parent = list(range(N + 1))
size = [1] * (N + 1)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]  # path halving
        x = parent[x]
    return x

def union(a, b):
    a = find(a); b = find(b)
    if a == b:
        return 0
    if size[a] < size[b]:
        a, b = b, a
    # 합치기 전의 쌍 증가량 = |A| * |B|
    inc = size[a] * size[b]
    parent[b] = a
    size[a] += size[b]
    return inc

# ----- 스윕 -----
pairs = 0          # 현재 (가중치 임계값 이상에서) 연결된 쌍의 수
ans = 0

for x, y, w in edges:
    inc = union(x, y)
    if inc:
        pairs += inc
    # 중요: 이 문제는 "병목 이하 모든 가중치"를 더하므로
    # 현재 임계값(=w)에서 연결된 전체 쌍 수 * w 를 더해야 함
    ans = (ans + w * pairs) % MOD

print(ans % MOD)
