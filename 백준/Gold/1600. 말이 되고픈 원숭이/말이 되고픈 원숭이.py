from collections import deque

k = int(input())  # 말처럼 이동 가능한 최대 횟수
w, h = map(int, input().split())  # w: 가로, h: 세로
grid = [[int(x) for x in input().split()] for _ in range(h)]  # 0: 평지, 1: 장애물

# 상하좌우 이동
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

# 말의 이동 (8방향)
horse_dxs = [2, 2, 1, 1, -1, -1, -2, -2]
horse_dys = [1, -1, 2, -2, 2, -2, 1, -1]

# 방문 배열: (x, y, 말처럼 이동한 횟수)에 대해 관리
visited = [[[False] * (k + 1) for _ in range(w)] for _ in range(h)]

# 범위 확인 함수
def in_range(x, y):
    return 0 <= x < w and 0 <= y < h

def bfs():
    q = deque()
    q.append((0, 0, 0))  # (x, y, 말처럼 이동한 횟수)
    visited[0][0][0] = True
    distance = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]
    
    while q:
        x, y, horse_moves = q.popleft()
        
        # 목적지에 도달하면 그때의 거리를 반환
        if x == w - 1 and y == h - 1:
            return distance[y][x][horse_moves]
        
        # 일반 이동 (상하좌우)
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            if in_range(new_x, new_y) and not visited[new_y][new_x][horse_moves] and grid[new_y][new_x] == 0:
                visited[new_y][new_x][horse_moves] = True
                distance[new_y][new_x][horse_moves] = distance[y][x][horse_moves] + 1
                q.append((new_x, new_y, horse_moves))
        
        # 말처럼 이동 (8방향)
        if horse_moves < k:  # 말처럼 이동할 횟수가 남아 있는 경우
            for dx, dy in zip(horse_dxs, horse_dys):
                new_x, new_y = x + dx, y + dy
                if in_range(new_x, new_y) and not visited[new_y][new_x][horse_moves + 1] and grid[new_y][new_x] == 0:
                    visited[new_y][new_x][horse_moves + 1] = True
                    distance[new_y][new_x][horse_moves + 1] = distance[y][x][horse_moves] + 1
                    q.append((new_x, new_y, horse_moves + 1))
    
    return -1  # 목적지에 도달할 수 없으면 -1 반환

# BFS 호출 및 결과 출력
print(bfs())
