# [level 3] 섬 연결하기 (프로그래머스 42861)
# 분류: 유니온파인드
# 접근: Union-Find로 연결성을 관리하며 그룹을 합치고 대표를 찾음

def solution(n, costs):
    result = 0
    parent = [0] * n
    costs.sort(key=lambda x: x[2])

    for i in range(n):
        parent[i] = i

    for a, b, cost in costs:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    return result

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b