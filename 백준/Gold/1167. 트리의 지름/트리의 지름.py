# [Gold II] 트리의 지름 (BOJ 1167)
# 분류: 그래프 이론, 그래프 탐색, 트리, 깊이 우선 탐색, 트리의 지름
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

import sys
sys.setrecursionlimit(10**5)

def dfs(idx, visited, total_value):
    global max_len, farthest_node

    visited.add(idx)
    if total_value > max_len:
        max_len = total_value
        farthest_node = idx

    for u, value in graph[idx]:
        if u not in visited:
            dfs(u, visited, total_value + value)

    visited.remove(idx)

V = int(input())
graph = {i: [] for i in range(1, V + 1)}
max_len = 0
farthest_node = 1  # 임의의 시작점

# 그래프 입력 받기
for _ in range(V):
    info = list(map(int, input().split()))
    u = info[0]
    edges = info[1:]
    idx = 0
    while edges[idx] != -1:
        v = edges[idx]
        value = edges[idx + 1]
        graph[u].append((v, value))
        idx += 2
# 첫 번째 DFS: 임의의 노드(1번 노드)에서 가장 먼 노드를 찾기
dfs(1, set(), 0)

# 두 번째 DFS: 가장 먼 노드에서 다시 DFS 실행
max_len = 0  # max_len을 초기화
dfs(farthest_node, set(), 0)

print(max_len)
