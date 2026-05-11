# [level 3] 등굣길 (프로그래머스 42898)
# 분류: DP
# 접근: 점화식 기반 dp 테이블을 채우며 최적해 누적



                        

def solution(m, n, puddles):
    # DP 테이블 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1  # 시작점

    # 물 웅덩이 위치를 -1로 설정
    for puddle in puddles:
        x, y = puddle
        dp[y][x] = -1

    # DP 테이블 채우기
    for row in range(1, n + 1):
        for col in range(1, m + 1):
            if dp[row][col] == -1:  # 물 웅덩이는 건너뜀
                dp[row][col] = 0
            elif row == 1 and col == 1:  # 시작점은 이미 설정됨
                continue
            else:
                # 위에서 오는 경우와 왼쪽에서 오는 경우를 더함
                if row > 1:
                    dp[row][col] += dp[row - 1][col]
                if col > 1:
                    dp[row][col] += dp[row][col - 1]
                
                # 1000000007로 나눈 나머지를 저장
                dp[row][col] %= 1000000007

    return dp[n][m]

