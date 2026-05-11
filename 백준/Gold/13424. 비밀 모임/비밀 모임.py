# [Gold IV] 비밀 모임 (BOJ 13424)
# 분류: 그래프 이론, 최단 경로, 데이크스트라, 플로이드–워셜
# 접근: 점화식 기반 dp 테이블을 채우며 최적해 누적

INF = float('inf')
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    dp = [[INF] * N for _ in range(N)]

    for _ in range(M):
        a, b, c = map(int, input().split())
        dp[a - 1][b - 1] = c
        dp[b - 1][a - 1] = c

    for i in range(N):
        dp[i][i] = 0

    K = int(input())
    loc = list(map(int, input().split()))

    for l in range(N):
        for i in range(N):
            for j in range(N):
                dp[i][j] = min(dp[i][l] + dp[l][j], dp[i][j])

    min_dist = INF
    min_s = -1
    for s in range(N):
        dist = 0
        for k in loc:
            dist += dp[s][k - 1]
        if min_dist > dist:
            min_dist = dist
            min_s = s

    print(min_s + 1)