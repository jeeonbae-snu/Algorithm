from collections import deque
import sys

input = sys.stdin.readline

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def find_area(sx, sy, visited, idx):
    visited[sy][sx] = True
    q = deque([(sx, sy)])
    board_id[sy][sx] = idx
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[ny][nx] and board[ny][nx] == 1:
                visited[ny][nx] = True
                board_id[ny][nx] = idx
                q.append((nx, ny))

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

# 1) 섬 라벨링: board_id[y][x]에 섬 번호 저장
board_id = [[0]*N for _ in range(N)]
visited = [[False]*N for _ in range(N)]
idx = 0
for y in range(N):
    for x in range(N):
        if board[y][x] == 1 and not visited[y][x]:
            idx += 1
            find_area(x, y, visited, idx)

# 2) 멀티소스 BFS: 모든 육지를 큐에 넣고 바다로 동시에 확장
owner = [[0]*N for _ in range(N)]   # 이 칸을 먼저 점유한 섬 번호
dist  = [[-1]*N for _ in range(N)]  # 가장 가까운 섬으로부터의 바다 거리
q = deque()

for y in range(N):
    for x in range(N):
        if board_id[y][x] != 0:
            owner[y][x] = board_id[y][x]
            dist[y][x] = 0
            q.append((x, y))

ans = float('inf')

while q:
    x, y = q.popleft()
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if not in_range(nx, ny):
            continue

        if dist[ny][nx] == -1:
            # 처음 방문: 바다 칸이므로 점유하고 확장
            owner[ny][nx] = owner[y][x]
            dist[ny][nx] = dist[y][x] + 1
            q.append((nx, ny))
        else:
            # 이미 방문된 칸: 다른 섬이 점유 중이면 만남 지점
            if owner[ny][nx] != owner[y][x]:
                ans = min(ans, dist[ny][nx] + dist[y][x])

print(0 if ans == float('inf') else ans)
