# [Gold III] 드래곤 커브 (BOJ 15685)
# 분류: 구현, 시뮬레이션
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

N = int(input())
visited = [[0] * 101 for _ in range(101)]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    dirs = [d]
    for _ in range(g):
        for dd in dirs[::-1]:
            dirs.append((dd + 1) % 4)
    visited[y][x] = 1
    sx, sy = x, y
    for dd in dirs:
        sx += dx[dd]
        sy += dy[dd]
        if 0 <= sx <= 100 and 0 <= sy <= 100:
            visited[sy][sx] = 1
count = 0
for i in range(100):
    for j in range(100):
        if visited[i][j] and visited[i + 1][j] and visited[i][j + 1] and visited[i + 1][j + 1]:
            count += 1
print(count)
