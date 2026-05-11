# [Gold I] 최솟값과 최댓값 (BOJ 2357)
# 분류: 세그먼트 트리, 자료 구조
# 접근: 인접 리스트 기반 그래프 탐색

def build(node, start, end):
    if start == end:
        tree[node] = (arr[start], arr[start])
    else:
        mid = (start + end) // 2
        build(node * 2, start, mid)
        build(node * 2 + 1, mid + 1, end)
        tree[node] = min(tree[node * 2][0], tree[node * 2 + 1][0]), max(tree[node * 2][1], tree[node * 2 + 1][1])

def query(node, start, end, left, right):
    if right < start or end < left:
        return float('inf'), - float('inf')

    if start >= left and end <= right:
        return tree[node]

    mid = (start + end) // 2
    lmin, lmax = query(node * 2, start, mid, left, right)
    rmin, rmax = query(node * 2 + 1, mid + 1, end, left, right)

    return min(lmin, rmin), max(lmax, rmax)

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
queries = []
for _ in range(M):
    a, b = map(int, input().split())
    queries.append((a - 1, b - 1))

tree = [(float('inf'), - float('inf')) for _ in range(4 * N)]
build(1, 0, N - 1)

for start, end in queries:
    print(*query(1, 0, N - 1, start, end))
