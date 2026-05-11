# [Gold IV] 미세먼지 안녕! (BOJ 17144)
# 분류: 구현, 시뮬레이션

import sys
input = sys.stdin.readline

def move_dust():
    new_home = [[0] * C for _ in range(R)]
    for y, x in purifiers:
        new_home[y][x] = -1
    for y in range(R):
        for x in range(C):
            if home[y][x] > 0:
                spread = home[y][x] // 5
                cnt = 0
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < C and 0 <= ny < R and home[ny][nx] != -1:
                        new_home[ny][nx] += spread
                        cnt += 1
                new_home[y][x] += home[y][x] - spread * cnt
    return new_home

def get_cycle_path(sx, sy, is_upper):
    path = []
    if is_upper:
        for x in range(sx + 1, C):
            path.append((x, sy))
        for y in range(sy - 1, -1, -1):
            path.append((C - 1, y))
        for x in range(C - 2, -1, -1):
            path.append((x, 0))
        for y in range(1, sy):
            path.append((0, y))
    else:
        for x in range(sx + 1, C):
            path.append((x, sy))
        for y in range(sy + 1, R):
            path.append((C - 1, y))
        for x in range(C - 2, -1, -1):
            path.append((x, R - 1))
        for y in range(R - 2, sy, -1):
            path.append((0, y))
    return path

def move_wind(path):
    prev = 0
    for x, y in path:
        home[y][x], prev = prev, home[y][x]

R, C, T = map(int, input().split())
home = [list(map(int, input().split())) for _ in range(R)]
purifiers = []
for y in range(R):
    for x in range(C):
        if home[y][x] == -1:
            purifiers.append((y, x))
purifier_up = purifiers[0][::-1]
purifier_down = purifiers[1][::-1]
upper_path = get_cycle_path(*purifier_up, is_upper=True)
lower_path = get_cycle_path(*purifier_down, is_upper=False)
for _ in range(T):
    home = move_dust()
    move_wind(upper_path)
    move_wind(lower_path)
total = sum(sum(cell for cell in row if cell > 0) for row in home)
print(total)
