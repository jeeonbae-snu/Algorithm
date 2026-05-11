def union(x, y):
    px = find(x)
    py = find(y)

    if px == py:
        return

    # Union by size: 작은 트리를 큰 트리 아래로 합침
    if size[px] > size[py]:
        parent[py] = px
        size[px] += size[py]  # 그룹 크기 합치기
    else:
        parent[px] = py
        size[py] += size[px]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]


T = int(input())
for i in range(T):
    F = int(input())
    parent = {}
    size = {}  # 각 집합의 크기를 추적

    for _ in range(F):
        x, y = input().split()

        if x not in parent:
            parent[x] = x
            size[x] = 1  # 초기 크기 1
        if y not in parent:
            parent[y] = y
            size[y] = 1  # 초기 크기 1

        union(x, y)

        # y의 루트를 찾고, 해당 루트의 크기 출력
        p = find(y)
        print(size[p])
