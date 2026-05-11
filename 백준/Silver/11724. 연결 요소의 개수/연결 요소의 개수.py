import sys
from collections import deque

def bfs(start, linked_list, visited):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        curr_v = q.popleft()
        for next_v in linked_list[curr_v]:
            if not visited[next_v]:
                visited[next_v] = True
                q.append(next_v)
    
    return 1

# 빠른 입력 처리
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
network = [tuple(map(int, line.split())) for line in data[1:m+1]]
visited = [False] * n 
linked_list = [[] for _ in range(n)]
count = 0

# 인접 리스트 생성
for start, end in network:
    linked_list[start - 1].append(end - 1)
    linked_list[end - 1].append(start - 1)

# 각 노드에 대해 bfs 수행
for k in range(n):
    if not visited[k]:
        count += bfs(k, linked_list, visited)

print(count)
