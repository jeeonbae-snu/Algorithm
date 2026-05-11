import heapq

def solve():
    N, M = map(int, input().split())
    board = [list(input().strip()) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'S':
                sy, sx = i, j
            if board[i][j] == 'F':
                fy, fx = i, j
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    # 각 칸에 [쓰레기수, 쓰레기옆수]의 최소값 기록
    dist = [[[float('inf'), float('inf')] for _ in range(M)] for _ in range(N)]
    hq = []
    heapq.heappush(hq, (0, 0, sy, sx))
    dist[sy][sx] = [0, 0]

    def is_near_garbage(y, x):
        for d in range(4):
            ny, nx = y+dy[d], x+dx[d]
            if 0 <= ny < N and 0 <= nx < M:
                if board[ny][nx] == 'g':
                    return True
        return False

    while hq:
        g_cnt, near_cnt, y, x = heapq.heappop(hq)
        if [g_cnt, near_cnt] > dist[y][x]:
            continue
        for d in range(4):
            ny, nx = y+dy[d], x+dx[d]
            if 0 <= ny < N and 0 <= nx < M:
                ng = g_cnt + (1 if board[ny][nx] == 'g' else 0)
                nn = near_cnt + (1 if board[ny][nx] == '.' and is_near_garbage(ny, nx) else 0)
                if [ng, nn] < dist[ny][nx]:
                    dist[ny][nx] = [ng, nn]
                    heapq.heappush(hq, (ng, nn, ny, nx))
    print(*dist[fy][fx])
solve()