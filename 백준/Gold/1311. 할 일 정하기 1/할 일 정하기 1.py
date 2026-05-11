# [Gold I] 할 일 정하기 1 (BOJ 1311)
# 분류: 다이나믹 프로그래밍, 비트마스킹, 비트필드를 이용한 다이나믹 프로그래밍
# 접근: 점화식 기반 dp 테이블을 채우며 최적해 누적

INF = 10_000_000
N = int(input())
M = 1 << N
cost = [list(map(int, input().split())) for _ in range(N)]
dp = [INF] * M
dp[0] = 0

for mask in range(1 << N):
    k = bin(mask).count("1")
    if k == N:
        continue

    for j in range(N):
        if mask & (1 << j):
            continue
        next_mask = mask | (1 << j)
        new_cost = dp[mask] + cost[k][j]
        if new_cost < dp[next_mask]:
            dp[next_mask] = new_cost

print(dp[M - 1])