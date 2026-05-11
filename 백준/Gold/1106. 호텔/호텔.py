import sys
input = sys.stdin.readline

C, N = map(int, input().split())
costs = [tuple(map(int, input().split())) for _ in range(N)]

# dp[i] = i명 이상의 고객을 만족시키는 최소비용
# (i < 0 인덱스 접근을 막기 위해 max(0, i - n) 사용)
dp = [float('inf')] * (C + 1)
dp[0] = 0

for i in range(1, C + 1):
    for cost, n in costs:
        prev = max(0, i - n)
        dp[i] = min(dp[i], dp[prev] + cost)

print(dp[C])