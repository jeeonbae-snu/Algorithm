# [Gold IV] 가장 긴 증가하는 부분 수열 4 (BOJ 14002)
# 분류: 다이나믹 프로그래밍, 역추적
# 접근: 점화식 기반 dp 테이블을 채우며 최적해 누적

N = int(input())
seq = list(map(int, input().split()))
dp = [[1, -1] for i in range(N)]

for i in range(1, N):
    for j in range(i):
        if seq[i] > seq[j] and dp[i][0] < dp[j][0] + 1:
                dp[i][0] = dp[j][0] + 1
                dp[i][1] = j

max_idx = max(range(N), key=lambda x: dp[x][0])
max_len = dp[max_idx][0]

path = []
cur = max_idx
while cur != -1:
    path.append(seq[cur])
    cur = dp[cur][1]

print(max_len)
print(*path[::-1])