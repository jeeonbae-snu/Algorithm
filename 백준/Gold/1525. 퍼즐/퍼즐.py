from collections import deque

# 이동할 수 있는 방향: 오른쪽, 아래, 왼쪽, 위
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

# 목표 상태
goal = '123456780'

def bfs(start):
    q = deque()
    q.append((start, 0))  # (퍼즐 상태, 이동 횟수)
    visited = set()
    visited.add(start)

    while q:
        state, count = q.popleft()

        if state == goal:  # 목표 상태에 도달하면 이동 횟수 반환
            return count

        zero_idx = state.index('0')  # 빈칸(0)의 위치 찾기
        x, y = zero_idx % 3, zero_idx // 3  # 1차원 문자열을 2차원 좌표로 변환

        # 상하좌우 탐색
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_zero_idx = new_y * 3 + new_x
                # 문자열에서 0과 새 좌표의 값을 교환
                new_state = list(state)
                new_state[zero_idx], new_state[new_zero_idx] = new_state[new_zero_idx], new_state[zero_idx]
                new_state = ''.join(new_state)

                if new_state not in visited:
                    visited.add(new_state)
                    q.append((new_state, count + 1))

    return -1  # 목표 상태에 도달할 수 없으면 -1 반환

# 초기 상태 입력
initial_state = ''
for _ in range(3):
    initial_state += ''.join(input().split())

# BFS 실행
print(bfs(initial_state))
