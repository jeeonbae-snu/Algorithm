import sys

input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    edges = []

    # 도로: 양방향 간선으로 추가
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))

    # 웜홀: 단방향 간선으로 추가, 이동 시 시간이 줄어드므로 가중치는 -T
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))

    # 모든 정점에 대해 초기 거리를 0으로 설정(더미 노드 효과)
    distances = [0] * (N + 1)  # 노드 번호는 1부터 N까지 사용
    negative_cycle = False

    # Bellman–Ford: N-1번 완화
    for _ in range(N - 1):
        for u, v, w in edges:
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    # 한 번 더 완화 시도: 더 갱신된다면 음수 사이클 존재
    for u, v, w in edges:
        if distances[u] + w < distances[v]:
            negative_cycle = True
            break

    print("YES" if negative_cycle else "NO")
