# [level 3] N으로 표현 (프로그래머스 42895)
# 분류: DP
# 접근: 점화식 기반 dp 테이블을 채우며 최적해 누적

def solution(N, number):
    if N == number:
        return 1
    
    dp = [set() for _ in range(9)]  

    for i in range(1, 9):
        dp[i].add(int(str(N) * i)) 

    for i in range(1, 9):
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i - j]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)

        if number in dp[i]:
            return i

    return -1

print(solution(5, 12))
