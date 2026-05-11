# [Gold I] 최종 순위 (BOJ 3665)
# 분류: 그래프 이론, 방향 비순환 그래프, 위상 정렬
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

from collections import deque

def topology_sort():
    q = deque()
    unique = True
    result = []

    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    while q:
        if len(q) > 1:
            unique = False
    
        curr_v = q.popleft()
        result.append(curr_v + 1)

        for next_v in graph[curr_v]:
            indegree[next_v] -= 1
            if indegree[next_v] == 0:
                q.append(next_v)

    return result, unique

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    rank = [int(x) - 1 for x in input().split()]
    m = int(input())
    exchanges = []
    for _ in range(m):
        i, j = map(int, input().split())
        exchanges.append([i - 1, j - 1])
    graph = {i: [] for i in range(n)}
    indegree = [0] * n

    for i, idx in enumerate(rank):
        graph[idx].extend(rank[i + 1:])

    for i, j in exchanges:
        if j in graph[i]:
            graph[j].append(i)
            graph[i].remove(j)
        else:
            graph[i].append(j)
            graph[j].remove(i)

    for i in range(n):
        for j in graph[i]:
            indegree[j] += 1

    result, unique = topology_sort()

    if len(result) == n:
        if unique:
            print(*result)
        else:
            print("?")
    else:
        print("IMPOSSIBLE")