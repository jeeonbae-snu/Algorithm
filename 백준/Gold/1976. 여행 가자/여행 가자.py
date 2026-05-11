# [Gold IV] 여행 가자 (BOJ 1976)
# 분류: 그래프 이론, 자료 구조, 그래프 탐색, 분리 집합
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

N = int(input())
M = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
parent = [x for x in range(N + 1)]
rank = [0] * (N + 1)

for i in range(N):
    for j in range(i):
        if info[i][j]:
            union(i + 1, j + 1)

plan = list(map(int, input().split()))
can_plan = True

p = find(plan[0])
for i in range(1, M):
    cur_p = find(plan[i])
    if p != cur_p:
        can_plan = False
        break
    p = cur_p
print("YES") if can_plan else print("NO")