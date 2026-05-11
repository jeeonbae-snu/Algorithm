# [Gold IV] 마법사 상어와 파이어볼 (BOJ 20056)
# 분류: 구현, 시뮬레이션

N, M, K = map(int, input().split())
fire_balls = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fire_balls.append((r - 1, c - 1, m, s, d))

directions = {
    0: (-1, 0),  
    1: (-1, 1),   
    2: (0, 1),    
    3: (1, 1),    
    4: (1, 0),   
    5: (1, -1),  
    6: (0, -1),  
    7: (-1, -1)   
}

for _ in range(K):
    temp = [[[] for _ in range(N)] for _ in range(N)]

    for r, c, m, s, d in fire_balls:
        dr, dc = directions[d]
        new_r = (r + s * dr) % N
        new_c = (c + s * dc) % N
        temp[new_r][new_c].append((m, s, d))

    fire_balls = []
    for r in range(N):
        for c in range(N):
            cell = temp[r][c]
            if len(cell) >= 2:
                l = len(cell)
                new_m = sum(x[0] for x in cell) // 5
                if new_m > 0:
                    new_s = sum(x[1] for x in cell) // l
                    if all(x[2] % 2 == cell[0][2] % 2 for x in cell):
                        for d in [0, 2, 4, 6]:
                            fire_balls.append((r, c, new_m, new_s, d))
                    else:
                        for d in [1, 3, 5, 7]:
                            fire_balls.append((r, c, new_m, new_s, d))
            elif len(cell) == 1:
                fire_balls.append((r, c, cell[0][0], cell[0][1], cell[0][2]))

total_m = sum(fb[2] for fb in fire_balls)
print(total_m)