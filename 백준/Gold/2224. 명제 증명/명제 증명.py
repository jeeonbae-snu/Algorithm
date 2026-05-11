# [Gold IV] 명제 증명 (BOJ 2224)
# 분류: 그래프 이론, 집합과 맵, 최단 경로, 플로이드–워셜
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

from collections import defaultdict, deque

X = int(input().strip())
adj = defaultdict(set)
nodes = set()

for _ in range(X):
    line = input().strip()
    p, q = line[0], line[-1]
    adj[p].add(q)
    nodes.add(p); nodes.add(q)
    
nodes = sorted(nodes)
reachable = set()

for s in nodes:
    visited = set([s])
    dq = deque(adj[s])
    while dq:
        v = dq.popleft()
        if v in visited:
            continue
        visited.add(v)
        reachable.add((s, v))
        for w in adj[v]:
            if w not in visited:
                dq.append(w)

print(len(reachable))
for p, q in sorted(reachable):
    print(f"{p} => {q}")