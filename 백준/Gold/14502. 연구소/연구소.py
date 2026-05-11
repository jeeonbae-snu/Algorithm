# [Gold IV] 연구소 (BOJ 14502)
# 분류: 구현, 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 너비 우선 탐색, 격자 그래프
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

from collections import deque
from itertools import combinations
import copy

def bfs(temp_board, start_points):
    visited = [[False] * M for _ in range(N)]
    q = deque(start_points)
    for x, y in start_points:
        visited[y][x] = True

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and temp_board[ny][nx] == 0:
                visited[ny][nx] = True
                q.append((nx, ny))

    return sum(row.count(True) for row in visited) - len(start_points)

N, M = map(int, input().split())
board = [[int(x) for x in input().split()] for _ in range(N)]
empty_spaces = []
virus_starts = []
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            empty_spaces.append((j, i))
        elif board[i][j] == 2:
            virus_starts.append((j, i))

max_safe_area = 0
for walls in combinations(empty_spaces, 3):
    temp_board = copy.deepcopy(board)
    for x, y in walls:
        temp_board[y][x] = 1

    virus_spread = bfs(temp_board, virus_starts)

    total_empty = len(empty_spaces)
    safe_area = total_empty - 3 - virus_spread
    max_safe_area = max(max_safe_area, safe_area)

print(max_safe_area)