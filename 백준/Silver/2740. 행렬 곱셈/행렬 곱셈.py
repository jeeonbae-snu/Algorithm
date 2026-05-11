# 행렬 A와 B의 크기 입력
N, M = map(int, input().split())  # 행렬 A의 크기
A = [list(map(int, input().split())) for _ in range(N)]  # 행렬 A의 원소 입력

# 행렬 B의 크기 입력
M2, K = map(int, input().split())  # 행렬 B의 크기
B = [list(map(int, input().split())) for _ in range(M2)]  # 행렬 B의 원소 입력

# 결과 행렬 C 초기화 (N x K 크기)
C = [[0] * K for _ in range(N)]

# 행렬 곱셈 수행
for i in range(N):
    for j in range(K):
        for k in range(M):
            C[i][j] += A[i][k] * B[k][j]

# 결과 행렬 C 출력
for row in C:
    print(*row)
