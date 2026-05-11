# [Silver IV] 상근이의 여행 (BOJ 9372)
# 분류: 그래프 이론, 트리
# 접근: Union-Find로 연결성을 관리하며 그룹을 합치고 대표를 찾음

def union(x, y):
    px = parent[x]
    py = parent[y]
    if px == py:
        return

    if size[px] >= size[py]:
        parent[py] = px
        size[px] += size[py]
    else:
        parent[px] = py
        size[py] += size[px]

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    flights = []
    for _ in range(M):
        a, b = map(int, input().split())
        flights.append((a - 1, b - 1))
    parent = [x for x in range(N)]
    size = [1] * N
    cnt = 0

    for u, v in flights:
        if find(u) != find(v):
            union(u, v)
            cnt += 1
            if cnt >= N - 1:
                break
    print(cnt)