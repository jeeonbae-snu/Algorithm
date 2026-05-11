r, c, target = map(int, input().split())
# 초기 배열은 3x3으로 입력받음
A = [list(map(int, input().split())) for _ in range(3)]
# 인덱스 조정을 위해 0-index로 변경
r, c = r - 1, c - 1

def operate_R(matrix):
    new_matrix = []
    max_len = 0
    for row in matrix:
        counts = {}
        # 0은 세지 않음
        for num in row:
            if num == 0:
                continue
            counts[num] = counts.get(num, 0) + 1
        # (숫자, 등장 횟수) 쌍을 등장 횟수, 숫자 순으로 정렬
        pairs = sorted(counts.items(), key=lambda x: (x[1], x[0]))
        new_row = []
        for num, cnt in pairs:
            new_row.extend([num, cnt])
        max_len = max(max_len, len(new_row))
        new_matrix.append(new_row)
    # 모든 행의 길이를 max_len에 맞춰 0으로 채우고, 100을 넘으면 자르기
    for i in range(len(new_matrix)):
        if len(new_matrix[i]) < max_len:
            new_matrix[i].extend([0] * (max_len - len(new_matrix[i])))
        if len(new_matrix[i]) > 100:
            new_matrix[i] = new_matrix[i][:100]
    return new_matrix

def operate_C(matrix):
    # 전치해서 각 행에 대해 R 연산을 적용한 후 다시 전치
    transposed = list(zip(*matrix))
    transposed = [list(row) for row in transposed]
    transposed = operate_R(transposed)
    new_matrix = list(zip(*transposed))
    new_matrix = [list(row) for row in new_matrix]
    return new_matrix

time = 0
while True:
    # 배열의 크기가 r, c보다 작으면 해당 위치는 0으로 간주
    if r < len(A) and c < len(A[0]) and A[r][c] == target:
        print(time)
        break
    if time > 100:
        print(-1)
        break

    # 행의 개수가 열의 개수보다 크거나 같으면 R 연산, 그렇지 않으면 C 연산
    if len(A) >= len(A[0]):
        A = operate_R(A)
    else:
        A = operate_C(A)
    time += 1
