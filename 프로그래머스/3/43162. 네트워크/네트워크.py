# [level 3] 네트워크 (프로그래머스 43162)
# 분류: BFS/DFS
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

from collections import deque

def bfs(start, computers, visited):
    q = deque([start])
    visited[start] = True
    
    while q:
        curr_v = q.popleft()
        
        for next_v in range(len(computers)):
            if computers[curr_v][next_v] == 1 and not visited[next_v]:
                visited[next_v] = True
                q.append(next_v)

def solution(n, computers):
    visited = [False] * n
    network_count = 0
    
    for i in range(n):
        if not visited[i]:
            bfs(i, computers, visited)
            network_count += 1
    
    return network_count
