from collections import deque

def solution(priorities, location):
    q = deque()
    
    # 문서의 우선순위와 원래 인덱스를 큐에 추가
    for i, p in enumerate(priorities):
        q.append((p, i))
    
    ans = 0  # 인쇄된 문서의 수
    while q:
        p, i = q.popleft()  # 큐에서 문서 가져오기
        # 현재 문서보다 우선순위가 높은 문서가 큐에 있는지 확인
        if any(p < qj[0] for qj in q):
            q.append((p, i))  # 현재 문서를 큐의 뒤로 보내기
        else:
            ans += 1  # 문서 인쇄
            # 인쇄한 문서가 우리가 찾고 있는 문서인지 확인
            if i == location:
                return ans  # 위치와 같으면 인쇄 순서 반환

print(solution([2, 1, 3, 2], 2))  # 결과: 1
print(solution([1, 1, 9, 1, 1, 1], 0))  # 결과: 5
