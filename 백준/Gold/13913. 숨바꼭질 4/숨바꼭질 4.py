from collections import deque

N, K = map(int, input().split())

# 1) N >= K: 단순 감소
if N >= K:
    print(N - K)          # 연산 횟수
    print(*range(N, K - 1, -1))  # N, N-1, ..., K
    exit()

# 2) N < K: BFS로 최단 경로
max_limit = 2 * K
dist = [-1] * (max_limit + 1)
prev = [-1] * (max_limit + 1)

dq = deque([N])
dist[N] = 0

while dq:
    x = dq.popleft()
    if x == K:
        break
    for nx in (x - 1, x + 1, x * 2):
        if 0 <= nx <= max_limit and dist[nx] == -1:
            dist[nx] = dist[x] + 1
            prev[nx] = x
            dq.append(nx)

# 결과 출력
print(dist[K])
path = []
cur = K
while cur != -1:
    path.append(cur)
    cur = prev[cur]
path.reverse()
print(*path)
