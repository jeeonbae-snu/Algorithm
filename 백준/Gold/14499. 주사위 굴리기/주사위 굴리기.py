# [Gold IV] 주사위 굴리기 (BOJ 14499)
# 분류: 구현, 시뮬레이션

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]
directions = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
for cmd in commands:
    dx, dy = directions[cmd]
    nx, ny = x + dx, y + dy
    if not (0 <= nx < N and 0 <= ny < M):
        continue
    if cmd == 1:
        new_top = dice[5]
        new_bottom = dice[4]
        new_east = dice[0]
        new_west = dice[1]
        new_north = dice[2]
        new_south = dice[3]
        dice = [new_top, new_bottom, new_north, new_south, new_east, new_west]
    elif cmd == 2:
        new_top = dice[4]
        new_bottom = dice[5]
        new_east = dice[1]
        new_west = dice[0]
        new_north = dice[2]
        new_south = dice[3]
        dice = [new_top, new_bottom, new_north, new_south, new_east, new_west]
    elif cmd == 3:
        new_top = dice[3]
        new_bottom = dice[2]
        new_north = dice[0]
        new_south = dice[1]
        new_east = dice[4]
        new_west = dice[5]
        dice = [new_top, new_bottom, new_north, new_south, new_east, new_west]
    elif cmd == 4:
        new_top = dice[2]
        new_bottom = dice[3]
        new_north = dice[1]
        new_south = dice[0]
        new_east = dice[4]
        new_west = dice[5]
        dice = [new_top, new_bottom, new_north, new_south, new_east, new_west]
    if board[nx][ny] == 0:
        board[nx][ny] = dice[1]
    else:
        dice[1] = board[nx][ny]
        board[nx][ny] = 0
    x, y = nx, ny
    print(dice[0])
