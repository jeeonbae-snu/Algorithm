from collections import deque

def solution(n, wires):
    min_len = []
    
    for wire in wires:
        # wires 리스트 복사 후 현재 wire 제거
        tmp = wires[:]
        tmp.remove(wire)
        
        # 네트워크 초기화
        network = [[] for _ in range(n)]
        
        # 네트워크 구축
        for start, end in tmp:
            network[start-1].append(end-1)
            network[end-1].append(start-1)
        
        # 첫 번째 네트워크 크기 계산
        def bfs(start):
            q = deque([start])
            visited[start] = True
            count = 1
            while q:
                curr_v = q.popleft()
                for next_v in network[curr_v]:
                    if not visited[next_v]:
                        visited[next_v] = True
                        q.append(next_v)
                        count += 1
            return count
        
        visited = [False] * n
        left_len = bfs(wire[0] - 1)  # 첫 번째 네트워크 크기
        
        # 전체 노드 수에서 left_len을 빼면 두 번째 네트워크 크기
        right_len = n - left_len
        
        # 두 네트워크 크기의 차이를 기록
        min_len.append(abs(left_len - right_len))
    
    return min(min_len)
