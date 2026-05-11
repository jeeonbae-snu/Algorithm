def solution(money):
    n = len(money)
    
    # 첫 번째 집을 선택한 경우
    dp1 = [0] * n
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    
    for i in range(2, n - 1):  # 마지막 집을 포함하지 않음
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
    
    # 첫 번째 집을 선택하지 않은 경우
    dp2 = [0] * n
    dp2[0] = 0
    dp2[1] = money[1]
    
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
    
    # 두 경우 중 최대값 반환
    return max(dp1[n-2], dp2[n-1])
