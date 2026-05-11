import sys
import heapq
input = sys.stdin.readline

def in_range(x, y, W, H):
    return 0 <= x < W and 0 <= y < H

def shortest_escape(sx, sy, board, costs, W, H):
    INF = float('inf')
    times = [[INF] * W for _ in range(H)]
    times[sy][sx] = 0
    hq = [(0, sx, sy)]
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    while hq:
        time, x, y = heapq.heappop(hq)
        if time > times[y][x]:
            continue

        # 여기가 바로 테두리라면 최단 탈출 시간 확정
        if x == 0 or x == W-1 or y == 0 or y == H-1:
            return time

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny, W, H):
                c = board[ny][nx]
                cost = costs.get(c, 0)
                nt = time + cost
                if nt < times[ny][nx]:
                    times[ny][nx] = nt
                    heapq.heappush(hq, (nt, nx, ny))
    return INF  # (이론상 닿을 수 없는 경우)

T = int(input())
for _ in range(T):
    K, W, H = map(int, input().split())
    costs = {}
    for _ in range(K):
        name, t = input().split()
        costs[name] = int(t)

    board = [list(input().rstrip()) for _ in range(H)]
    # 시작점(E) 찾기
    for y in range(H):
        for x in range(W):
            if board[y][x] == 'E':
                sx, sy = x, y
                break

    ans = shortest_escape(sx, sy, board, costs, W, H)
    print(ans)
