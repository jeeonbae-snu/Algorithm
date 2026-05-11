import sys
from collections import deque

input = sys.stdin.readline

# 입력: N(열), M(행)
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]

# 방향: W(1), N(2), E(4), S(8)
dirs = [(-1, 0, 1), (0, -1, 2), (1, 0, 4), (0, 1, 8)]

room_id = [[-1]*N for _ in range(M)]
room_sizes = []

def bfs(sr, sc, rid):
    q = deque([(sr, sc)])
    room_id[sr][sc] = rid
    size = 0
    while q:
        r, c = q.popleft()
        size += 1
        cell = grid[r][c]
        for dx, dy, bit in dirs:
            nr, nc = r + dy, c + dx   # 주의: r=행(y), c=열(x)
            if 0 <= nr < M and 0 <= nc < N:
                # 해당 방향에 벽이 없으면 이동 가능
                if (cell & bit) == 0 and room_id[nr][nc] == -1:
                    room_id[nr][nc] = rid
                    q.append((nr, nc))
    return size

# 1) 방 라벨링 및 각 방 넓이
rid = 0
for r in range(M):
    for c in range(N):
        if room_id[r][c] == -1:
            room_sizes.append(bfs(r, c, rid))
            rid += 1

num_rooms = rid
max_room = max(room_sizes) if room_sizes else 0

# 2) 벽 하나 제거하여 얻을 수 있는 최대 방 크기
max_merge = 0
for r in range(M):
    for c in range(N):
        id1 = room_id[r][c]
        cell = grid[r][c]
        for dx, dy, bit in dirs:
            nr, nc = r + dy, c + dx
            if 0 <= nr < M and 0 <= nc < N:
                id2 = room_id[nr][nc]
                if id1 != id2:
                    # 두 다른 방 사이의 벽 하나를 허문다고 가정
                    # (실제 그 방향에 벽이 있든 없든 합 최대만 보면 충분)
                    max_merge = max(max_merge, room_sizes[id1] + room_sizes[id2])

print(num_rooms)
print(max_room)
print(max_merge)
