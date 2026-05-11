# [Silver III] 계단 오르기 (BOJ 2579)
# 분류: 다이나믹 프로그래밍
# 접근: 점화식 기반 dp 테이블을 채우며 최적해 누적

import sys

input = sys.stdin.readline

n = int(input().strip())
score = [int(input().strip()) for _ in range(n)]

if n == 0:
    print(0)
elif n == 1:
    print(score[0])
elif n == 2:
    print(score[0] + score[1])
else:
    dp = [0] * n
    dp[0] = score[0]
    dp[1] = score[0] + score[1]
    dp[2] = max(score[0] + score[2], score[1] + score[2])

    for i in range(3, n):
        dp[i] = max(dp[i - 2] + score[i], dp[i - 3] + score[i - 1] + score[i])

    print(dp[n - 1])
