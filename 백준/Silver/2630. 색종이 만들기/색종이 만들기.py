def is_same(grid):
    """grid가 모두 같은 색이면 True, 아니면 False를 반환합니다."""
    color = grid[0][0]
    for row in grid:
        for val in row:
            if val != color:
                return False
    return True


def divide(grid):
    n = len(grid)
    # 기저조건: grid가 모두 같은 색이면 해당 색종이 1장을 반환합니다.
    if is_same(grid):
        # 0: 흰색, 1: 파란색
        return (1, 0) if grid[0][0] == 0 else (0, 1)

    mid = n // 2
    # grid를 4분할합니다.
    top_left = [row[:mid] for row in grid[:mid]]
    top_right = [row[mid:] for row in grid[:mid]]
    bottom_left = [row[:mid] for row in grid[mid:]]
    bottom_right = [row[mid:] for row in grid[mid:]]

    # 각 분할 영역을 재귀적으로 처리합니다.
    first = divide(top_left)
    second = divide(top_right)
    third = divide(bottom_left)
    fourth = divide(bottom_right)

    # 네 영역의 결과를 합칩니다.
    return conquer(first, second, third, fourth)


def conquer(first, second, third, fourth):
    """각 영역의 (흰색, 파란색) 개수를 합산하여 반환합니다."""
    white = first[0] + second[0] + third[0] + fourth[0]
    blue = first[1] + second[1] + third[1] + fourth[1]
    return (white, blue)


# 입력 처리
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# 재귀 호출하여 결과 도출
white_count, blue_count = divide(grid)

print(white_count)
print(blue_count)
