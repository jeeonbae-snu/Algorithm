n = int(input())
m = int(input())
INF = float('inf')

# 1) cost와 next 행렬 초기화
cost = [[INF]*n for _ in range(n)]
next_node = [[None]*n for _ in range(n)]
for i in range(n):
    cost[i][i] = 0
    next_node[i][i] = i

# 2) 간선 입력
for _ in range(m):
    u, v, w = map(int, input().split())
    u, v = u-1, v-1
    if cost[u][v] > w:
        cost[u][v] = w
        next_node[u][v] = v

# 3) 플로이드–워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            if cost[i][k] + cost[k][j] < cost[i][j]:
                cost[i][j] = cost[i][k] + cost[k][j]
                next_node[i][j] = next_node[i][k]

# 4) 결과 출력
# (1) 거리
for i in range(n):
    for j in range(n):
        print(0 if cost[i][j] == INF else cost[i][j], end=' ')
    print()

# 4-2) 경로 정보 출력 (총 n*n줄)
for i in range(n):
    for j in range(n):
        if cost[i][j] == INF or i == j:
            # 경로가 없거나 (i==j) 스킵: 문제에서 i→i 경로를 0으로 간주
            print(0)
        else:
            # 경로 재구성
            path = [i]
            cur = i
            while cur != j:
                cur = next_node[cur][j]
                path.append(cur)
            # 1-indexed로 변환
            path = [x+1 for x in path]
            # k = 경로상의 도시 수
            print(len(path), *path)