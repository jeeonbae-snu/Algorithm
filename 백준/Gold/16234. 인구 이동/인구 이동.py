# [Gold IV] 인구 이동 (BOJ 16234)
# 분류: 구현, 그래프 이론, 그래프 탐색, 시뮬레이션, 너비 우선 탐색
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

from collections import deque
import sys

input = sys.stdin.readline

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sy][sx] = True
    total_pop = A[sy][sx]
    cells = [(sx, sy)]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if (in_range(nx, ny) and not visited[ny][nx] and
                    L <= abs(A[ny][nx] - A[y][x]) <= R):
                visited[ny][nx] = True
                total_pop += A[ny][nx]
                q.append((nx, ny))
                cells.append((nx, ny))

    avg_pop = total_pop // len(cells)
    for x, y in cells:
        A[y][x] = avg_pop

    return len(cells) > 1

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
day = 0

while True:
    visited = [[False] * N for _ in range(N)]
    moved = False

    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                if bfs(x, y):
                    moved = True

    if not moved:
        break
    day += 1

print(day)