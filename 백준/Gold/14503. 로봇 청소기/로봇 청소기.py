# 로봇 청소기가 작동을 시작한 후 작동을 멈출 때 까지 청소하는 칸의 개수
N, M = map(int, input().split())
r, c, d = map(int, input().split())  # 0: 북, 1: 동, 2: 남, 3: 서
tiles = [[int(x) for x in input().split()] for _ in range(N)]
dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]
cnt = 0

while True:
    if tiles[r][c] == -1:  # 현재 칸이 청소된 경우
        can_go = False
        for i in range(1, 5):
            nd = (d - i + 4) % 4  # 반시계 방향으로 90도 회전
            nx, ny = c + dxs[nd], r + dys[nd]
            if (0 <= nx < M and 0 <= ny < N) and tiles[ny][nx] != 1:
                if tiles[ny][nx] != -1:
                    tiles[ny][nx] = -1
                    cnt += 1
                    c, r, d = nx, ny, nd  # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
                    can_go = True
                    break
        if not can_go:
            nx, ny = c - dxs[d], r - dys[d]
            if (0 <= nx < M and 0 <= ny < N) and tiles[ny][nx] != 1:  # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
                c, r = nx, ny
            else:
                break

    elif tiles[r][c] == 0:  # 현재 칸이 청소되지 않은 경우
        tiles[r][c] = -1
        cnt += 1

print(cnt)
