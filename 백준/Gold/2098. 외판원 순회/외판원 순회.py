import sys
input = sys.stdin.readline
N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
INF = float('inf')
M = 1 << N

# dp[mask][i]: mask 비트마스크에 표시된 도시들을 모두 방문했고, 마지막에 도시 i에 머물러 있을 때의 최소 비용
dp = [[INF] * N for _ in range(M)]
# 출발지는 0번 도시로 가정
dp[1 << 0][0] = 0

for mask in range(M):
    for i in range(N):
        if dp[mask][i] == INF:
            continue
        # i에서 j로 가보자
        for j in range(N):
            if mask & (1 << j):  # 이미 방문했다면 skip
                continue
            if cost[i][j] == 0:  # 경로가 없으면 skip
                continue
            next_mask = mask | (1 << j)
            dp[next_mask][j] = min(dp[next_mask][j], dp[mask][i] + cost[i][j])

# 모든 도시 방문한 상태에서 다시 0으로 돌아오는 최소 비용 계산
full_mask = (1 << N) - 1
answer = INF
for i in range(N):
    if cost[i][0] == 0:
        continue
    answer = min(answer, dp[full_mask][i] + cost[i][0])

print(answer)
