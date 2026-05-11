# [Silver III] 바이러스 (BOJ 2606)
# 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

from collections import deque

n = int(input()) #NUM VERTEX
m = int(input()) #NUM EDGE
networks = [[int(x) for x in input().split()] for _ in range(m)]
visited = [False] * n
linked_list = [[] for _ in range(n)]  

for start, end in networks:
    linked_list[start - 1].append(end - 1)
    linked_list[end - 1].append(start - 1)

def bfs():
    q = deque()
    q.append(0)
    visited[0] = True
    
    count = 0
    while q:
        curr_v = q.popleft()
        for next_v in range(n):
            if not visited[next_v] and next_v in linked_list[curr_v]:
                visited[next_v] = True
                count += 1
                q.append(next_v)
                
    return count 

print(bfs())