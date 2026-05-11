# [Gold III] 감시 (BOJ 15683)
# 분류: 구현, 브루트포스 알고리즘, 시뮬레이션, 백트래킹
# 접근: Union-Find로 연결성을 관리하며 그룹을 합치고 대표를 찾음

def get_area(x, y, d):
    path = set()
    while True:
        nx, ny = x + dxs[d], y + dys[d]
        if 0 <= nx < M and 0 <= ny < N and board[ny][nx] != 6:
            x, y = nx, ny
            path.add((nx, ny))
        else:
            break
    return path

def select_area(selected_path, t):
    global max_area
    if t == cnt:
        max_area = max(len(selected_path), max_area)
        return
    n = len(total_path[t])
    for i in range(n):
        union_path = selected_path.union(total_path[t][i])
        select_area(union_path, t+1)

N, M = map(int, input().split())
board = [[int(x) for x in input().split()] for _ in range(N)]
total_path = {}
cnt = 0
max_area = 0
dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]
n_wall = 0
for y in range(N):
    for x in range(M):
        if board[y][x] == 1:  # 한 방향 -> 네 개 고려
            temp_ = []
            for d in range(4):
                temp = {(x, y)}
                temp = temp.union(get_area(x, y, d))
                temp_.append(temp)
            total_path[cnt] = temp_
            cnt += 1
        elif board[y][x] == 2:  # 일자 두 방향 -> 두 개 고려
            temp_ = []
            for d in range(2):
                temp = {(x, y)}
                temp = temp.union(get_area(x, y, d))
                temp = temp.union(get_area(x, y, (d + 6) % 4))
                temp_.append(temp)
            total_path[cnt] = temp_
            cnt += 1
        elif board[y][x] == 3:
            temp_ = []# 직각 두 방향 -> 네 개 고려
            for d in range(4):
                temp = {(x, y)}
                temp = temp.union(get_area(x, y, d))
                temp = temp.union(get_area(x, y, (d + 5) % 4))
                temp_.append(temp)
            total_path[cnt] = temp_
            cnt += 1
        elif board[y][x] == 4:  # 세 방향 -> 네 개 고려
            temp_ = []
            for rd in range(4):
                temp = {(x, y)}
                ds = [0, 1, 2, 3]
                ds.remove(rd)
                for d in ds:
                    temp = temp.union(get_area(x, y, d))
                temp_.append(temp)
            total_path[cnt] = temp_
            cnt += 1
        elif board[y][x] == 5:  # 모든 방향 -> 한 개 고려
            temp = {(x, y)}
            for d in range(4):
                temp = temp.union(get_area(x, y, d))
            total_path[cnt] = [temp]
            cnt += 1
        elif board[y][x] == 6:
            n_wall += 1
select_area(set(),0)
print(N*M-max_area-n_wall)