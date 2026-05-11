def rotate_clockwise(state):
    return state[N-1:] + state[:N-1]

def rotate_counterclockwise(state): 
    return state[1:] + state[:1]

# 입력 처리
states = [[int(x) for x in input().strip()] for _ in range(4)]
K = int(input())
rotates = [tuple(map(int, input().split())) for _ in range(K)]
N = 8

def rotate_gear(gear_idx, direction, states):
    directions = [0] * 4  # 0: 회전 안 함, 1: 시계, -1: 반시계
    directions[gear_idx] = direction

    # 왼쪽으로 연쇄 확인
    for i in range(gear_idx - 1, -1, -1):
        if states[i][2] != states[i + 1][6]:  # 맞물리는 극이 다르면
            directions[i] = -directions[i + 1]  # 반대 방향으로 회전
        else:
            break  # 같으면 연쇄 중단

    # 오른쪽으로 연쇄 확인
    for i in range(gear_idx + 1, 4):
        if states[i - 1][2] != states[i][6]:  # 맞물리는 극이 다르면
            directions[i] = -directions[i - 1]  # 반대 방향으로 회전
        else:
            break  # 같으면 연쇄 중단

    # 회전 적용
    for i in range(4):
        if directions[i] == 1:
            states[i] = rotate_clockwise(states[i])
        elif directions[i] == -1:
            states[i] = rotate_counterclockwise(states[i])

# 모든 회전 명령 처리
for idx, d in rotates:
    rotate_gear(idx - 1, d, states) 

# 점수 계산
score = sum(2**i if states[i][0] == 1 else 0 for i in range(4))
print(score)