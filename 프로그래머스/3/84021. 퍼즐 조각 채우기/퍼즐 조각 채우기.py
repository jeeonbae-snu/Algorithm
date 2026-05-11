from collections import deque

# 좌표가 범위 내에 있는지 확인하는 함수
def in_range(x, y, n, m):
    return 0 <= x < m and 0 <= y < n

# 블록을 BFS로 탐색하면서 정규화된 블록 좌표를 반환하는 함수
def bfs_and_normalize(start_y, start_x, board, visited, n, m, board_type):
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    
    block = []  # 블록의 좌표를 저장
    q = deque()
    q.append((start_x, start_y))
    visited[start_y][start_x] = True
    
    # 블록의 좌표 중 가장 작은 y, x를 추적
    block.append((0, 0))  # 시작 좌표를 (0, 0)으로 설정
    
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            if in_range(new_x, new_y, n, m) and not visited[new_y][new_x] and board[new_y][new_x] == board_type:
                visited[new_y][new_x] = True
                # 상대 좌표를 저장
                block.append((new_y - start_y, new_x - start_x))
                q.append((new_x, new_y))
                
    return block  # 이미 정규화된 블록 좌표 반환

# 블록을 좌상단으로 정렬하는 함수 (좌표 이동)
def normalize_block(block):
    block.sort()  # 좌표를 정렬하여 첫 번째 좌표를 기준으로 이동
    min_y, min_x = block[0]
    return [(y - min_y, x - min_x) for y, x in block]

# 블록을 90도 회전시키는 함수
def rotate_block(block):
    return [(-x, y) for y, x in block]  # 90도 회전

# 블록의 모든 회전 형태를 반환하는 함수
def get_rotations(block):
    rotations = []
    current_block = block
    for _ in range(4):  # 0도, 90도, 180도, 270도 회전
        normalized_block = normalize_block(current_block)
        rotations.append(normalized_block)
        current_block = rotate_block(current_block)
    return rotations

# 블록을 문자열로 변환해 해시값으로 변환
def block_to_string(block):
    return ''.join(f"{y},{x};" for y, x in block)

# 블록의 회전된 형태들 중 가장 작은 해시값을 반환
def get_block_hashes(block):
    rotations = get_rotations(block)
    cached_hashes = set()  # 회전된 블록의 해시값을 저장
    for rot in rotations:
        normalized_block = normalize_block(rot)
        block_hash = block_to_string(normalized_block)
        cached_hashes.add(block_hash)
    return min(cached_hashes)  # 가장 작은 해시값 반환

# 블록 리스트를 게임 보드에서 추출하는 함수
def extract_blocks(board, n, m, board_type):
    visited = [[False for _ in range(m)] for _ in range(n)]  # 방문 여부를 저장
    blocks = []
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == board_type and not visited[i][j]:
                block = bfs_and_normalize(i, j, board, visited, n, m, board_type)
                blocks.append((get_block_hashes(block), len(block)))  # 해시와 블록의 면적을 함께 저장
    
    return blocks

# 퍼즐을 맞추는 함수
def match_blocks(game_board_blocks, table_blocks):
    used = [False] * len(table_blocks)  # 테이블의 블록 사용 여부를 추적
    matched_area = 0

    for board_block, board_size in game_board_blocks:
        for i, (table_block, table_size) in enumerate(table_blocks):
            if used[i]:  # 이미 사용된 블록은 건너뜀
                continue
            # 크기 먼저 비교
            if board_size != table_size:
                continue
            if board_block == table_block:  # 해시값이 동일하면 매칭 성공
                used[i] = True
                matched_area += board_size  # 블록의 면적만큼 더함
                break  # 해당 블록과 매칭이 완료되면 다음으로 넘어감
    
    return matched_area

# 메인 솔루션 함수
def solution(game_board, table):
    n = len(game_board)
    m = len(game_board[0])
    
    # 게임 보드에서 빈 공간 블록(0) 추출
    game_board_blocks = extract_blocks(game_board, n, m, 0)
    
    # 테이블에서 퍼즐 조각 블록(1) 추출
    table_blocks = extract_blocks(table, n, m, 1)
    
    # 블록 매칭 후 맞춘 영역의 합 계산
    total_matched_area = match_blocks(game_board_blocks, table_blocks)
    
    return total_matched_area
