from collections import deque

n = int(input())
p1, p2 = map(int, input().split())  # 관계를 계산해야하는 사람의 번호
m = int(input())  # 부모 자식간 관계의 개수
networks = [[int(x) for x in input().split()] for _ in range(m)]
array = [[0 for _ in range(n)] for _ in range(n)]
visited = [False] * n
distance = [-1] * n  # 거리 배열을 -1로 초기화 (방문하지 않음을 나타냄)

# 부모 자식 간 관계 저장
for parent, child in networks:
    array[parent - 1][child - 1] = 1
    array[child - 1][parent - 1] = 1

# BFS 함수
def bfs():
    q = deque()
    q.append(p1 - 1)
    visited[p1 - 1] = True
    distance[p1 - 1] = 0  # 시작점의 거리는 0으로 설정

    while q:
        curr_v = q.popleft()
        for next_v in range(n):
            if not visited[next_v] and array[curr_v][next_v] != 0:
                visited[next_v] = True
                distance[next_v] = distance[curr_v] + 1
                q.append(next_v)
    
    if visited[p2 - 1]:
        return distance[p2 - 1]  # p2까지의 거리 반환
    else:
        return -1  # p2에 도달할 수 없을 경우 -1 반환

# 결과 출력
print(bfs())
