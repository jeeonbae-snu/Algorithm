N = int(input())
dp = [float('INF')] * (N + 1)
prev = [-1] * (N + 1)  # 경로 추적을 위한 배열
dp[1] = 0

for i in range(1, N + 1):
    if i * 2 <= N and dp[i * 2] > dp[i] + 1:
        dp[i * 2] = dp[i] + 1
        prev[i * 2] = i
    if i * 3 <= N and dp[i * 3] > dp[i] + 1:
        dp[i * 3] = dp[i] + 1
        prev[i * 3] = i
    if i + 1 <= N and dp[i + 1] > dp[i] + 1:
        dp[i + 1] = dp[i] + 1
        prev[i + 1] = i

# 경로 복원
path = []
cur = N
while cur != -1:
    path.append(cur)
    cur = prev[cur]

# 결과 출력
print(dp[N])          # 최소 연산 횟수
print(*path)  # 경로
