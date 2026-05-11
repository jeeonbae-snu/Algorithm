MOD = 1000000000  # 큰 수 방지

n = int(input())

# DP 테이블 초기화: dp[i][j]는 i자리 계단 수 중 마지막 숫자가 j인 경우의 개수
dp = [[0] * 10 for _ in range(n+1)]

# 한 자리 숫자는 모두 계단 수
for j in range(1, 10):
    dp[1][j] = 1

# DP 점화식 적용
for i in range(2, n+1):
    for j in range(10):
        if j > 0:
            dp[i][j] += dp[i-1][j-1]  # j-1에서 오는 경우
        if j < 9:
            dp[i][j] += dp[i-1][j+1]  # j+1에서 오는 경우
        dp[i][j] %= MOD  # 큰 수 방지

# n자리 계단 수의 개수 합산
result = sum(dp[n]) % MOD
print(result)