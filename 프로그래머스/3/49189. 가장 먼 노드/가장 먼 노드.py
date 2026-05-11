# [level 3] 가장 먼 노드 (프로그래머스 49189)
# 분류: BFS/DFS, 그래프
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

from collections import deque

def solution(n, edge):
    visited = [False] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    depth = [0] * (n + 1)
    
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    q = deque()
    q.append(1)
    visited[1] = True
    depth[1] = 0
    
    while q:
        curr_v = q.popleft()
        
        for next_v in graph[curr_v]:
            if not visited[next_v]:
                visited[next_v] = True
                depth[next_v] = depth[curr_v] + 1
                q.append(next_v)
                
    max_distance = max(depth)
    return depth.count(max_distance)