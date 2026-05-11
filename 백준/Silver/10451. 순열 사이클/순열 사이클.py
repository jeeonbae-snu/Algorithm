# [Silver III] 순열 사이클 (BOJ 10451)
# 분류: 그래프 이론, 그래프 탐색, 순열 사이클 분할
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

from collections import deque

def bfs(start, linked_list):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        curr_v = q.popleft()
        for i, next_v in enumerate(linked_list[curr_v]):
            if not visited[next_v] and linked_list[curr_v][i]:
                visited[next_v] = True
                q.append(next_v)
    
    return 1

T = int(input())
n = []
p = []

for i in range(T):
    n.append(int(input()))
    p.append([int(x) for x in input().split()])

for j in range(T):
    linked_list = [[] for _ in range(n[j])]
    visited = [False] * n[j]
    count = 0

    for start, end in enumerate(p[j]):
        linked_list[start].append(end - 1)
        linked_list[end - 1].append(start)

    for k in range(n[j]):
        if not visited[k]:
            count += bfs(k, linked_list)

    print(count)
