# [Gold IV] 사촌 (BOJ 9489)
# 분류: 자료 구조, 트리
# 접근: Union-Find로 연결성을 관리하며 그룹을 합치고 대표를 찾음

from collections import defaultdict

while True:
    n, k = map(int, input().split())
    if (n, k) == (0, 0):
        exit()
    arr = list(map(int, input().split()))

    parent = defaultdict(int)
    idx = 0

    for i in range(1, n):
        parent[arr[i]] = arr[idx]
        if i < n - 1 and arr[i] + 1 < arr[i + 1]:
            idx += 1

    cnt = 0
    p = parent[k]
    gp = parent[p]

    if gp:
        for elem in arr:
            np = parent[elem]
            ngp = parent[np]

            if gp ==  ngp and p != np:
                cnt += 1

    print(cnt)