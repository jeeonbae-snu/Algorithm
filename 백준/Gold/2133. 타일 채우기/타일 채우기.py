N = int(input().strip())

# 3×N 타일 채우기는 N이 홀수면 방법이 0개
if N % 2 == 1:
    print(0)
    exit()

# dp[0]=1, dp[2]=3을 기저로 사용
dp = [0] * (max(N, 2) + 1)
dp[0] = 1
dp[2] = 3

# 간단한 등가 점화식: dp[n] = 4*dp[n-2] - dp[n-4]
for n in range(4, N + 1, 2):
    dp[n] = 4 * dp[n - 2] - dp[n - 4]

print(dp[N])