# [Gold V] 집합의 표현 (BOJ 1717)
# 분류: 자료 구조, 분리 집합
# 접근: Union-Find로 연결성을 관리하며 그룹을 합치고 대표를 찾음

def union(e1, e2):
    r1 = find(e1)
    r2 = find(e2)

    if r1 == r2:
        return False

    if rank[r1] < rank[r2]:
        parent[r1] = r2
    elif rank[r1] > rank[r2]:
        parent[r2] = r1
    else:
        parent[r2] = r1
        rank[r1] += 1

    return True

def find(e):
    if parent[e] != e:
        parent[e] = find(parent[e])
    return parent[e]

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)
for _ in range(m):
    op, e1, e2 = map(int, input().split())
    if op == 0:
        union(e1, e2)
    elif op == 1:
        print("YES" if find(e1) == find(e2) else "NO")