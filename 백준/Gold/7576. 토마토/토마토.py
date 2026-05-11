from collections import deque

m, n = map(int, input().split())  # M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수
grid = [[int(x) for x in input().split()] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
day = [[-1 for _ in range(m)] for _ in range(n)]  # day 배열을 -1로 초기화
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]  # 상하좌우 방향

def in_range(x, y):
    return 0 <= x < m and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and not visited[y][x] and grid[y][x] != -1

# BFS에서 여러 시작점(익은 토마토, 값이 1인 위치)을 큐에 넣고 탐색
def bfs():
    q = deque()

    # 모든 시작점(익은 토마토, 값이 1인 위치)을 큐에 넣고 BFS 시작
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                q.append((j, i))  # (x, y) 형태로 큐에 추가
                visited[i][j] = True
                day[i][j] = 0  # 시작점의 day는 0으로 설정

    # BFS 탐색 시작
    while q:
        x, y = q.popleft()

        # 상하좌우로 이동 가능한 곳 탐색
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            if can_go(new_x, new_y):
                visited[new_y][new_x] = True
                day[new_y][new_x] = day[y][x] + 1  # 현재 노드에서 +1일 경과
                q.append((new_x, new_y))

    # BFS 종료 후, 최대 일수 및 익지 않은 토마토 확인
    max_days = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:  # 익지 않은 토마토(처리되지 않은 부분)
                if day[i][j] == -1:  # 도달할 수 없는 토마토가 있다면
                    return -1
                max_days = max(max_days, day[i][j])  # 최댓값 갱신

    return max_days

# BFS를 호출하고 결과 출력
print(bfs())
