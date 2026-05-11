from collections import deque

N = int(input())
grid = [[int(x) for x in input().split()] for _ in range(N)]
time = 0
eat = 0
volume = 2

# 상어 위치 찾기
shark = (-1, -1)
for y in range(N):
    for x in range(N):
        if grid[y][x] == 9:
            shark = (x, y)
            grid[y][x] = 0  # 상어 위치를 빈 칸으로 초기화

dx = [-1, 0, 1, 0]  # 좌, 상, 우, 하
dy = [0, -1, 0, 1]


def bfs(start_x, start_y, volume):
    visited = [[False] * N for _ in range(N)]
    queue = deque([(start_x, start_y, 0)])  # (x, y, distance)
    visited[start_y][start_x] = True
    possible_fish = []

    while queue:
        x, y, dist = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx]:
                # 이동 가능 조건: 빈 칸이거나, 자신보다 작은 물고기
                if grid[ny][nx] <= volume:
                    visited[ny][nx] = True
                    queue.append((nx, ny, dist + 1))
                    # 먹을 수 있는 물고기라면
                    if 0 < grid[ny][nx] < volume:
                        possible_fish.append((dist + 1, ny, nx))

    if not possible_fish:
        return None
    # 거리, y, x 순으로 정렬하여 가장 가까운 물고기 선택
    possible_fish.sort()
    return possible_fish[0]  # (distance, y, x)


while True:
    # BFS로 먹을 수 있는 물고기 찾기
    result = bfs(shark[0], shark[1], volume)

    # 더 이상 먹을 물고기가 없으면 종료
    if result is None:
        break

    dist, ny, nx = result
    # 상어 이동
    shark = (nx, ny)
    # 물고기 먹기
    grid[ny][nx] = 0
    time += dist
    eat += 1

    # 크기 증가 체크
    if eat == volume:
        volume += 1
        eat = 0

print(time)