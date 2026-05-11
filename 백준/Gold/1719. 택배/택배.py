# [Gold III] 택배 (BOJ 1719)
# 분류: 그래프 이론, 최단 경로, 데이크스트라, 플로이드–워셜
# 접근: 점화식 기반 dp 테이블을 채우며 최적해 누적

INF = float('inf')
n, m = map(int, input().split())
dp = [[INF] * n for _ in range(n)]
next_node = [[-1] * n for _ in range(n)]

for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1; v -= 1
    dp[u][v] = w
    dp[v][u] = w
    next_node[u][v] = v
    next_node[v][u] = u

for i in range(n):
    dp[i][i] = 0
    next_node[i][i] = i

for k in range(n):
    for i in range(n):
        for j in range(n):
            new_dist = dp[i][k] + dp[k][j]
            if new_dist < dp[i][j]:
                dp[i][j] = new_dist
                next_node[i][j] = next_node[i][k]

# 결과 출력: 첫번째로 거쳐야 할 정점 행렬 (1-indexed, 대각선 및 경로 없으면 '-')
for i in range(n):
    for j in range(n):
        if i == j or next_node[i][j] == -1:
            print('-', end=' ')
        else:
            print(next_node[i][j] + 1, end=' ')
    print()
