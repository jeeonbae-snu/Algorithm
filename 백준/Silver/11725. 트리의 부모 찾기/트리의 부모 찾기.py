from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
parent  = [0]     * (N+1)

q = deque([1])
visited[1] = True

while q:
    v = q.popleft()
    for w in graph[v]:
        if not visited[w]:
            visited[w]  = True
            parent[w]   = v
            q.append(w)

# 2번 노드부터 N번 노드까지 부모 출력
for i in range(2, N+1):
    print(parent[i])
