# [Gold I] 구간 합 구하기 (BOJ 2042)
# 분류: 세그먼트 트리, 자료 구조
# 접근: 인접 리스트 기반 그래프 탐색

def build(node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        build(node * 2, start, mid)
        build(node * 2 + 1, mid + 1, end)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]

def query(node, start, end, left, right):
    if right < start or end < left:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    lsum = query(node * 2, start, mid, left, right)
    rsum = query(node * 2 + 1, mid + 1, end, left, right)
    return lsum + rsum

def update(node, start, end, idx, diff):
    if idx < start or idx > end:
        return

    tree[node] += diff

    if start != end:
        mid = (start + end) // 2
        update(node * 2, start, mid, idx, diff)
        update(node * 2 + 1, mid + 1, end, idx, diff)

N, M, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
op = []
tree = [0] * (4 * N)
build(1, 0, N - 1)
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        idx = b - 1
        diff = c - arr[idx]
        arr[idx] = c
        update(1, 0, N - 1, idx, diff)
    elif a == 2:
        print(query(1, 0, N - 1, b - 1, c - 1))