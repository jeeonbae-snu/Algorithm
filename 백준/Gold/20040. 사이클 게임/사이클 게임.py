# [Gold IV] 사이클 게임 (BOJ 20040)
# 분류: 자료 구조, 분리 집합
# 접근: Union-Find로 연결성을 관리하며 그룹을 합치고 대표를 찾음

def union(x, y):
    px = find(x)
    py = find(y)
    if px == py:
        return
    if rank[px] > rank[py]:
        parent[py] = px
    elif rank[px] < rank[py]:
        parent[px] = py
    else:
        parent[py] = px
        rank[px] += 1

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

N, M = map(int, input().split())
parent = [x for x in range(N)]
rank = [0] * N

for i in range(M):
    x, y = map(int, input().split())
    if find(x) == find(y):
        print(i + 1)
        exit()
    union(x, y)
print(0)
