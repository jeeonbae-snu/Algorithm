import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
T = 1

def dfs(v, parent):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            if not dfs(u, v):
                return False  # 하위에서 사이클이 발견되면 거짓 반환
        elif u != parent:
            # 이미 방문된 정점인데, 부모가 아니라면 사이클
            return False
    return True  # 더 이상 탐색할 곳 없으면 이 컴포넌트는 트리

while True:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break

    graph = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)
    tree_count = 0

    for node in range(1, n + 1):
        if not visited[node]:
            # 새 컴포넌트 시작 → 사이클 없으면 트리 개수 +1
            if dfs(node, parent=0):
                tree_count += 1

    # 결과 출력
    print(f'Case {T}:', end=' ')
    if tree_count == 0:
        print("No trees.")
    elif tree_count == 1:
        print("There is one tree.")
    else:
        print(f"A forest of {tree_count} trees.")

    T += 1