# [level 3] 여행경로 (프로그래머스 43164)
# 분류: BFS/DFS
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

def dfs(curr_trip, tickets, path, used_tickets):
    if len(path) == len(tickets) + 1:  # 모든 티켓을 사용한 경우
        return path

    for i, ticket in enumerate(tickets):
        if not used_tickets[i] and curr_trip == ticket[0]:  # 아직 사용되지 않았고, 출발지가 현재 위치와 일치하는 티켓
            used_tickets[i] = True
            result = dfs(ticket[1], tickets, path + [ticket[1]], used_tickets)
            if result:  # 경로가 유효하다면 반환
                return result
            used_tickets[i] = False  # 경로가 유효하지 않다면 다시 사용 가능하도록 설정
            
    return None  # 경로가 유효하지 않으면 None 반환

def solution(tickets):
    tickets.sort()  # 사전순 정렬
    used_tickets = [False] * len(tickets)  # 각 티켓 사용 여부를 기록
    return dfs("ICN", tickets, ["ICN"], used_tickets)
