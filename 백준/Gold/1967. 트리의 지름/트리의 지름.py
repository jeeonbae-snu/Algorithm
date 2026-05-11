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


n = int(input())
graph = {i: [] for i in range(1, n + 1)}
max_len = 0
farthest_node = 1  # 임의의 시작점

# 그래프 입력 받기
for _ in range(n - 1):
    u, v, value = map(int, input().split())
    graph[u].append((v, value))
    graph[v].append((u, value))

# 첫 번째 DFS: 임의의 노드(1번 노드)에서 가장 먼 노드를 찾기
dfs(1, set(), 0)

# 두 번째 DFS: 가장 먼 노드에서 다시 DFS 실행
max_len = 0  # max_len을 초기화
dfs(farthest_node, set(), 0)

print(max_len)
