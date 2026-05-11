from collections import deque

def topology_sort():
    q = deque()
    result = []

    # 진입 차수가 0인 노드를 큐에 추가
    for i in range(N):
        if indegree[i] == 0:
            q.append(i)

    while q:
        curr_v = q.popleft()
        result.append(curr_v + 1)  # 출력용으로 +1 (1-based)

        for next_v in graph[curr_v]:
            indegree[next_v] -= 1
            if indegree[next_v] == 0:
                q.append(next_v)

    return result

# 입력 처리
N, M = map(int, input().split())
graph = {i: [] for i in range(N)}
indegree = [0] * N

for _ in range(M):
    i, j = map(int, input().split())
    graph[i - 1].append(j - 1)  # 1-based를 0-based로 변환
    indegree[j - 1] += 1

# 위상 정렬 수행
result = topology_sort()

# 결과 출력
if len(result) == N:  # 모든 노드가 정렬되었다면
    print(*result)
else:  # 사이클이 존재하는 경우
    print("Cycle exists, no valid topological sort possible")