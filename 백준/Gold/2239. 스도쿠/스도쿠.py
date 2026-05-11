def find_empty(board):
    """빈 칸(0) 중에서 (y, x)를 하나 찾아 반환. 없으면 None."""
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                return y, x
    return None

def is_valid(board, y, x, v):
    """board[y][x]에 v를 놓아도 되는지 검사."""
    # 가로 검사
    if v in board[y]:
        return False
    # 세로 검사
    for i in range(9):
        if board[i][x] == v:
            return False
    # 3×3 블록 검사
    by, bx = (y // 3) * 3, (x // 3) * 3
    for i in range(by, by + 3):
        for j in range(bx, bx + 3):
            if board[i][j] == v:
                return False
    return True

def backtrack(board):
    """백트래킹으로 스도쿠를 풀고, 성공 시 True를 반환."""
    empty = find_empty(board)
    if not empty:
        return True    # 빈 칸이 더 이상 없으면 완성
    y, x = empty

    for v in range(1, 10):
        if is_valid(board, y, x, v):
            board[y][x] = v
            if backtrack(board):
                return True
            board[y][x] = 0   # 되돌리기

    return False   # 1~9 중 어느 것도 통과 못 하면 상위 호출로 백트랙

board = [list(map(int, input().strip())) for _ in range(9)]

if backtrack(board):
    for row in board:
        for v in row:
            print(v, end='')
        print()
