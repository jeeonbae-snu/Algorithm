# [Gold IV] 알파벳 (BOJ 1987)
# 분류: 그래프 이론, 그래프 탐색, 깊이 우선 탐색, 백트래킹, 격자 그래프
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

def in_range(x, y):
    return 0 <= x < C and 0 <= y < R

def dfs(x, y, visited, find):
    global ans

    ans = max(ans, len(find))

    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and not visited[ny][nx] and board[ny][nx] not in find:
            visited[ny][nx] = True
            find.add(board[ny][nx])
            dfs(nx, ny, visited, find)
            visited[ny][nx] = False
            find.remove(board[ny][nx])

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
ans = 0
visited[0][0] = True
dfs(0, 0, visited, {board[0][0]})
print(ans)