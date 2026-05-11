from collections import deque

n, m, v = map(int, input().split())
table = [[int(x) for x in input().split()] for _ in range(m)]
visited = [False] * n
linked_list = [[] for _ in range(n)]

def dfs(curr_v, answer):
    visited[curr_v] = True  # 첫 번째 방문 처리 추가
    for next_v in linked_list[curr_v]:
        if not visited[next_v]:
            visited[next_v] = True
            answer.append(next_v + 1)
            dfs(next_v, answer)  # 재귀 호출만 하고 반환값은 따로 처리하지 않음
    return answer

def bfs(curr_v):
    q = deque()
    q.append(curr_v)
    visited[curr_v] = True  # True/False로 통일
    answer = [curr_v + 1]
    
    while q:
        curr_v = q.popleft()
        for next_v in linked_list[curr_v]:
            if not visited[next_v]:
                visited[next_v] = True  # True/False로 통일
                answer.append(next_v + 1)
                q.append(next_v)
                
    return answer

for start, end in sorted(table):
    linked_list[start - 1].append(end - 1)
    linked_list[end - 1].append(start - 1)
    
for i in range(n):
    linked_list[i].sort()

# DFS 수행
visited[v - 1] = True
print(*dfs(v - 1, [v]))

# BFS 수행을 위해 visited 초기화
visited = [False] * n
print(*bfs(v - 1))
