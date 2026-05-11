from collections import deque

def bfs(start, target):
    # 예외 처리: start가 target과 같으면 바로 0 반환
    if start == target:
        return 0
    
    # 큐에 (현재 값, 연산 횟수)를 저장
    q = deque()
    q.append((start, 0))
    
    # 방문 여부 확인 (탐색 범위를 target의 두 배까지만 허용)
    max_limit = max(target * 2, start)
    visited = [False] * (max_limit + 1)
    visited[start] = True
    
    while q:
        curr, depth = q.popleft()
        
        # 세 가지 연산: +1, *2, -1
        for next_value in (curr + 1, curr * 2, curr - 1):
            # 타겟에 도달하면 바로 최소 연산 횟수 반환
            if next_value == target:
                return depth + 1
            
            # 범위 내에서 탐색하고, 음수 값과 이미 방문한 값은 무시
            if 0 <= next_value <= max_limit and not visited[next_value]:
                visited[next_value] = True
                q.append((next_value, depth + 1))
    
    return -1  # 도달할 수 없는 경우

# 입력 처리
start, target = map(int, input().split())
# 최소 연산 횟수 출력
print(bfs(start, target))
