import sys
import heapq

input = sys.stdin.readline

# Read inputs
N, M, A, B, C = map(int, input().split())
A -= 1
B -= 1

# Build graph and collect all edge weights
graph = [[] for _ in range(N)]
all_weights = set()
for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append((v, w))
    graph[v].append((u, w))
    all_weights.add(w)

# If there are no edges, cannot reach
if not all_weights:
    print(-1)
    sys.exit(0)

# Sort unique weights for binary search
sorted_ws = sorted(all_weights)
INF = float('inf')

# Check if path exists with max edge weight <= X and total cost <= C
def can_go(X):
    dist = [INF] * N
    dist[A] = 0
    pq = [(0, A)]  # (current cost, node)
    while pq:
        cost, u = heapq.heappop(pq)
        if cost > dist[u]:
            continue
        for v, w in graph[u]:
            if w > X:
                continue
            nc = cost + w
            if nc < dist[v] and nc <= C:
                dist[v] = nc
                heapq.heappush(pq, (nc, v))
    return dist[B] <= C

# Binary search on the max edge weight
answer = -1
lo, hi = 0, len(sorted_ws) - 1
while lo <= hi:
    mid = (lo + hi) // 2
    X = sorted_ws[mid]
    if can_go(X):
        answer = X
        hi = mid - 1
    else:
        lo = mid + 1

print(answer)
