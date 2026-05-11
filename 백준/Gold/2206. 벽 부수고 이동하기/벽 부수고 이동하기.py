from collections import deque
import math

def can_go(x, y):
    return 0 <= x < m and 0 <= y < n

def bfs(init_x, init_y):
    q = deque()
    q.append((init_x, init_y, False))  # False: 점프를 아직 안 했음
    visit[0][0][0] = True  # (0, 0) 점프 안 했을 때 방문 표시
    distance[0][0][0] = 1

    while q:
        x, y, jumped = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            if can_go(new_x, new_y):
                if grid[new_y][new_x] == 0 and not visit[new_y][new_x][jumped]:
                    # 빈 칸 이동
                    visit[new_y][new_x][jumped] = True
                    distance[new_y][new_x][jumped] = distance[y][x][jumped] + 1
                    q.append((new_x, new_y, jumped))
                elif grid[new_y][new_x] == 1 and not jumped and not visit[new_y][new_x][1]:
                    # 벽인데 점프 가능
                    visit[new_y][new_x][1] = True
                    distance[new_y][new_x][1] = distance[y][x][jumped] + 1
                    q.append((new_x, new_y, True))

n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]
# 3차원 visit과 distance 배열
visit = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
distance = [[[math.inf for _ in range(2)] for _ in range(m)] for _ in range(n)]
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

bfs(0, 0)

# 도착점의 최단 거리 계산
res_no_jump = distance[n-1][m-1][0]
res_jump = distance[n-1][m-1][1]
result = min(res_no_jump, res_jump)

# 도달 불가능한 경우 처리
if result == math.inf:
    print(-1)
else:
    print(result)
