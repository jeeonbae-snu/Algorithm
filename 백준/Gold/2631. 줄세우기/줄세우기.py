import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [int(input().strip()) for _ in range(N)]

# dp[i] = i번째 원소로 끝나는 최장 증가 부분수열(LIS) 길이
dp = [1] * N
for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:          # 엄격 증가
            dp[i] = max(dp[i], dp[j] + 1)

lis_len = max(dp)
print(N - lis_len)  # 최소 이동 