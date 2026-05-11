# [level 5] 방의 개수 (프로그래머스 49190)
# 분류: BFS/DFS
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사


#     # 이동 방향에 대한 x, y 좌표 변화 (8방향)
    
#     # 노드와 간선 저장
    
#     # 시작 위치
#     x, y = 0, 0
#     visited_nodes.add((x, y))
    
#         # 같은 방향으로 두 번 이동하여 중간 노드 고려
#             nx, ny = x + dxs[d], y + dys[d]
            
#             # 간선이 새로운 경로로 만들어지면서 이미 방문한 노드를 재방문하는 경우, 방 생성
            
#             # 노드와 간선을 방문 처리
#             visited_nodes.add((nx, ny))
#             visited_edges.add(((x, y), (nx, ny)))
#             visited_edges.add(((nx, ny), (x, y)))
            
#             # 위치 갱신
#             x, y = nx, ny

# # print(solution([6, 6, 6, 4, 4, 4, 0, 0, 0, 2, 2, 2]))  # 예상 출력: 방의 개수
from collections import defaultdict

def solution(arrows):
    # 이동 방향에 대한 x, y 좌표 변화 (8방향)
    dxs = [0, 1, 1, 1, 0, -1, -1, -1]
    dys = [1, 1, 0, -1, -1, -1, 0, 1]
    
    # 노드와 간선 저장
    visited_nodes = set()  # 방문한 노드
    visited_edges = set()  # 방문한 간선 (노드 사이 경로)
    
    # 시작 위치
    x, y = 0, 0
    visited_nodes.add((x, y))
    
    # 노드와 간선의 개수 추적
    V = 1  # 초기 노드 개수 (시작점)
    E = 0  # 초기 간선 개수
    
    for d in arrows:
        # 같은 방향으로 두 번 이동하여 중간 노드 고려
        for _ in range(2):
            nx, ny = x + dxs[d], y + dys[d]
            
            # 새로운 노드 발견 시
            if (nx, ny) not in visited_nodes:
                visited_nodes.add((nx, ny))
                V += 1  # 노드 개수 증가
            
            # 새로운 간선 발견 시
            if ((x, y), (nx, ny)) not in visited_edges:
                visited_edges.add(((x, y), (nx, ny)))
                visited_edges.add(((nx, ny), (x, y)))  # 양방향으로 처리
                E += 1  # 간선 개수 증가
            
            # 위치 갱신
            x, y = nx, ny

    # 오일러 공식을 이용해 면(F)의 개수를 계산
    F = E - V + 2

    # 방의 개수는 F - 1 (외곽 면을 제외)
    return F - 1
