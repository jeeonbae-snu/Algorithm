import sys
input = sys.stdin.readline

N = int(input())
# dims[i] = (행, 열) of matrix i
dims = [tuple(map(int, input().split())) for _ in range(N)]

# dp[i][j]: i번째 행렬부터 j번째 행렬까지 곱하는 최소 비용
# i == j 일 땐 곱할 게 없으므로 0
dp = [[0 if i == j else float('inf') for j in range(N)] for i in range(N)]

# chain_length = 2부터 N까지 늘려가며 계산
for chain_len in range(2, N + 1):
    for i in range(0, N - chain_len + 1):
        j = i + chain_len - 1
        # i..j 구간을 (i..k)와 (k+1..j)로 나누는 모든 k 시도
        for k in range(i, j):
            # 곱셈 비용 = (i..k) 결과의 행 * (i..k) 결과의 열 * (k+1..j) 결과의 열
            # dims[i][0] = i번째 행렬의 행
            # dims[k][1] = k번째 행렬의 열 = (i..k) 결과의 열
            # dims[j][1] = j번째 행렬의 열 = (k+1..j) 결과의 열
            cost = dp[i][k] + dp[k+1][j] + dims[i][0] * dims[k][1] * dims[j][1]
            if cost < dp[i][j]:
                dp[i][j] = cost

print(dp[0][N-1])
