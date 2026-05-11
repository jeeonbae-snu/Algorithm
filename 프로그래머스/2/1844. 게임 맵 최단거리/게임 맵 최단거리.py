# [level 2] 게임 맵 최단거리 (프로그래머스 1844)
# 분류: BFS/DFS
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

from collections import deque

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]  # 방향 (오른쪽, 아래, 왼쪽, 위)

def bfs(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]  # 방문 여부 매번 초기화
    distance = [[-1 for _ in range(m)] for _ in range(n)]  # 각 좌표까지의 최단 거리 기록
    
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    distance[0][0] = 1  # 시작점의 거리 1로 초기화 (첫 칸 포함)

    while q:
        y, x = q.popleft()
        
        for dy, dx in zip(dys, dxs):
            new_y, new_x = y + dy, x + dx
            if can_go(new_y, new_x, maps, visited, n, m):
                visited[new_y][new_x] = True 
                distance[new_y][new_x] = distance[y][x] + 1  # 새로운 좌표까지의 거리 갱신
                q.append((new_y, new_x))
                
    # # 목적지에 도달할 수 없는 경우 -1 반환

    return distance[n - 1][m - 1]  # 목적지까지의 거리 반환

def in_range(y, x, n, m):
    return 0 <= y < n and 0 <= x < m 

def can_go(y, x, maps, visited, n, m):
    return in_range(y, x, n, m) and not visited[y][x] and maps[y][x] 

def solution(maps):
    return bfs(maps)  # 최단 경로 길이 계산
