import sys

input = sys.stdin.readline
n, k = map(int, input().split())
dp = [float('inf')] * (k + 1) # 가치 v를 만들기 위해 필요한 동전의 최소 개수
coins = []

for _ in range(n):
    c = int(input())
    if 0 <= c <= k:
        coins.append(c)
        dp[c] = 1

for i in range(1, k + 1):
    for j in range(1, i):
        dp[i] = min(dp[i - j] + dp[j], dp[i])

print(-1) if dp[k] == float('inf') else print(dp[k])