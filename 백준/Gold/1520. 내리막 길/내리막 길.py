# [Gold III] 내리막 길 (BOJ 1520)
# 분류: 다이나믹 프로그래밍, 그래프 이론, 그래프 탐색, 깊이 우선 탐색
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# 입력: M행 N열
M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

# 1) Top-Down DFS + Memoization Solution
dp_memo = [[-1] * N for _ in range(M)]

def dfs(x: int, y: int) -> int:
    '''
    (x, y)에서 (N-1, M-1)까지 도달 가능한 경로의 개수를 반환
    메모이제이션을 사용하여 중복 탐색 방지
    '''
    # 도착 지점이면 1 반환
    if x == N - 1 and y == M - 1:
        return 1
    # 이미 계산된 값이 있으면 재활용
    if dp_memo[y][x] != -1:
        return dp_memo[y][x]

    dp_memo[y][x] = 0
    # 사방탐색으로 내리막 조건 만족 시 재귀 호출
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and board[y][x] > board[ny][nx]:
            dp_memo[y][x] += dfs(nx, ny)

    return dp_memo[y][x]

# 2) Bottom-Up DP using Topological Order by Height
# 모든 칸을 높이 순으로 정렬하여 DP 갱신 순서 보장
# cells.sort(reverse=True)  # 높이 내림차순
# # 시작점에서 출발하는 경로 1개로 초기화
#     # 시작점에서 이 칸까지 올 수 있는 경로가 없다면 무시
#     # 내리막 이동 가능한 이웃 칸에 경로 수 전파
#         nx, ny = x + dx, y + dy

# 결과 출력
# Top-Down DFS + Memo 결과
print(dfs(0, 0))
# Bottom-Up DP 결과
