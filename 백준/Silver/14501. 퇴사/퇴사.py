N = int(input())
info = []
for _ in range(N):
    info.append(list(map(int, input().split())))

dp = [0] * (N + 1) 

for i in range(N):
    dp[i + 1] = max(dp[i + 1], dp[i])
    time, reward = info[i][0], info[i][1]
    if i + time <= N:  
        dp[i + time] = max(dp[i + time], dp[i] + reward)

print(dp[N])