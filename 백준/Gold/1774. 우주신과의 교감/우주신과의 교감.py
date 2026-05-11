import sys, math
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
coords = [tuple(map(int, input().split())) for _ in range(N)]
# 이미 연결된 간선은 (u,v), (v,u) 쌍으로 set에 저장
connected = set()
for _ in range(M):
    u, v = map(int, input().split())
    connected.add((u-1, v-1))
    connected.add((v-1, u-1))

# Prim 준비
visited = [False] * N
min_edge = [float('inf')] * N
min_edge[0] = 0.0    # 임의의 시작점(0번)에서 출발

total_cost = 0.0

for _ in range(N):
    # 아직 MST에 포함되지 않은 정점 중 가장 작은 min_edge를 고른다
    u = min(
        (i for i in range(N) if not visited[i]),
        key=lambda i: min_edge[i]
    )
    visited[u] = True
    total_cost += min_edge[u]

    ux, uy = coords[u]
    # u를 추가했으니, 아직 방문 안 한 모든 v에 대해 간선(u,v)로 업데이트
    for v in range(N):
        if not visited[v]:
            # 이미 연결된 간선이면 0, 아니면 유클리드 거리
            w = 0.0 if (u, v) in connected else math.hypot(ux - coords[v][0], uy - coords[v][1])
            if w < min_edge[v]:
                min_edge[v] = w

# 결과 출력 (소수점 둘째 자리까지)
print(f"{total_cost:.2f}")
