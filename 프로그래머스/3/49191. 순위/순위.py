from collections import deque

def solution(n, results):
    victory = [[] for _ in range(n)]
    lose = [[] for _ in range(n)]
    
    for v, l in results:
        victory[v - 1].append(l - 1)
        lose[l - 1].append(v - 1)

    ans = 0
    for i in range(n):
        visited = set()
        # 승리 경로 탐색
        q = deque([i])
        while q:
            player = q.popleft()
            for winner in victory[player]:
                if winner not in visited:
                    visited.add(winner)
                    q.append(winner)
        # 패배 경로 탐색
        q = deque([i])
        while q:
            player = q.popleft()
            for loser in lose[player]:
                if loser not in visited:
                    visited.add(loser)
                    q.append(loser)
        
        # 순위가 명확한 경우
        if len(visited) == n - 1:
            ans += 1

    return ans

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))  # 예상 출력: 2
