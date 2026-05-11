n = int(input())
m = int(input())
INF = float('inf')

# 1) cost와 next 행렬 초기화
cost = [[INF]*n for _ in range(n)]
for i in range(n):
    cost[i][i] = 0

# 2) 간선 입력
for _ in range(m):
    u, v, w = map(int, input().split())
    u, v = u-1, v-1
    if cost[u][v] > w:
        cost[u][v] = w

# 3) 플로이드–워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            if cost[i][k] + cost[k][j] < cost[i][j]:
                cost[i][j] = cost[i][k] + cost[k][j]

# 4) 결과 출력
for i in range(n):
    for j in range(n):
        print(0 if cost[i][j] == INF else cost[i][j], end=' ')
    print()
