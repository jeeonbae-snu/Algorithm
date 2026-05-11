import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

MOD = 1_000_000_007

def build(node, start, end):
    if start == end:
        tree[node] = arr[start] % MOD
    else:
        mid = (start + end) // 2
        build(node * 2,     start, mid)
        build(node * 2 + 1, mid + 1, end)
        tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % MOD

def query(node, start, end, left, right):
    # 완전히 벗어날 때
    if right < start or end < left:
        return 1
    # 완전히 포함될 때
    if left <= start and end <= right:
        return tree[node]
    # 부분 겹칠 때
    mid = (start + end) // 2
    l = query(node * 2,     start, mid, left, right)
    r = query(node * 2 + 1, mid + 1, end, left, right)
    return (l * r) % MOD

def update(node, start, end, idx, new_val):
    # 영향을 받지 않는 구간이면 종료
    if idx < start or idx > end:
        return
    if start == end:
        # 리프 노드에 새 값 저장
        tree[node] = new_val % MOD
    else:
        mid = (start + end) // 2
        update(node * 2,     start, mid, idx, new_val)
        update(node * 2 + 1, mid + 1, end, idx, new_val)
        # 두 자식 노드값 곱해서 갱신
        tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % MOD

# 입력 처리
N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [0] * (4 * N)

# 초기 빌드
build(1, 0, N - 1)

# 연산 수행
for _ in range(M + K):
    typ, b, c = map(int, input().split())
    idx = b - 1
    if typ == 1:
        # arr[idx] 값을 c로 변경
        arr[idx] = c
        update(1, 0, N - 1, idx, c)
    else:  # typ == 2
        # 구간 [b-1, c-1]의 곱 출력
        res = query(1, 0, N - 1, b - 1, c - 1)
        print(res)

        