# [level 3] 입국심사 (프로그래머스 43238)
# 분류: 투포인터
# 접근: 두 포인터를 이동시키며 구간 합/조건 계산

def solution(n, times):
    left = 1
    right = max(times) * n
    
    while left <= right:
        people = 0
        mid = (left + right) // 2
        for time in times:
            people += mid // time
            if people >= n:
                break
        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer