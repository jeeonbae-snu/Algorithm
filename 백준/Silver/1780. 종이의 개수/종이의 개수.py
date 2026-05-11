# [Silver II] 종이의 개수 (BOJ 1780)
# 분류: 분할 정복, 재귀

def is_same_num(x, y, n):
    init_num = matrix[y][x]
    for dy in range(n):
        for dx in range(n):
            if matrix[y + dy][x + dx] != init_num:
                return False
    return True

def divide_paper(x, y, n):
    global cnt_minus_one, cnt_zero, cnt_one
    if is_same_num(x, y, n):
        if matrix[y][x] == 1:
            cnt_one += 1
        elif matrix[y][x] == 0:
            cnt_zero += 1
        elif matrix[y][x] == -1:
            cnt_minus_one += 1
        return
    new_size = n // 3
    for i in range(3):
        for j in range(3):
            divide_paper(x + i * new_size, y + j * new_size, new_size)

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
cnt_minus_one = 0
cnt_zero = 0
cnt_one = 0
divide_paper(0, 0, n)
print(cnt_minus_one)
print(cnt_zero)
print(cnt_one)
