# [level 1] 체육복 (프로그래머스 42862)

def solution(n, lost, reserve):
    ans = 0

    for i in range(1, n + 1):
        if i in lost and i in reserve:
            reserve.remove(i)
            lost.remove(i)

    for i in range(1, n + 1):
        if i in lost:
            if i - 1 in reserve:
                reserve.remove(i - 1)
                ans += 1
            elif i + 1 in reserve:
                reserve.remove(i + 1)
                ans += 1
        else:
            ans += 1
    return ans

