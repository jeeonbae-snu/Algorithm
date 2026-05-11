import sys, heapq

INF = 10**18
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

def in_range(x, y, N):
    # 좌표가 보드 범위 안에 있는지 확인
    return 0 <= x < N and 0 <= y < N

def dijkstra(N, T, board):
    # dist[y][x][k] = (x, y)에 이동횟수 % 3 == k 인 상태로 도착하는 최소 시간
    dist = [[[INF] * 3 for _ in range(N)] for __ in range(N)]
    dist[0][0][0] = 0  # 시작점, 이동횟수 0, 시간 0
    pq = [(0, 0, 0, 0)]  # (시간, x, y, 이동횟수%3)

    while pq:
        t, x, y, k = heapq.heappop(pq)

        # 이미 더 빠른 경로가 있으면 스킵
        if t != dist[y][x][k]:
            continue

        # 4방향 이동
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not in_range(nx, ny, N):
                continue

            nt = t + T  # 기본 이동 시간 추가
            nk = (k + 1) % 3  # 이동 횟수 % 3 업데이트

            # 이동 후 3의 배수가 되는 순간, 땅의 추가 시간 더하기
            if nk == 0:
                nt += board[ny][nx]

            # 더 짧은 시간이면 갱신
            if nt < dist[ny][nx][nk]:
                dist[ny][nx][nk] = nt
                heapq.heappush(pq, (nt, nx, ny, nk))

    # 도착 지점(N-1, N-1)에 도착하는 세 가지 경우 중 최소값 반환
    return min(dist[N - 1][N - 1])

# 입력 처리
input = sys.stdin.readline
N, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(dijkstra(N, T, board))
