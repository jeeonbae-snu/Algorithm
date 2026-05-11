def solution(triangle):
    n = len(triangle)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    dp[1][1] = triangle[0][0]
    
    for i in range(2, n):
        dp[i][1] = dp[i-1][1] + triangle[i-1][0]
        dp[i][i] = dp[i-1][i-1] + triangle[i-1][i-1]
        
    for i in range(3, n+1):
        for j in range(2, i):
            dp[i][j] = max(dp[i-1][j-1] + triangle[i-1][j-1], dp[i-1][j] + triangle[i-1][j-1])
            
    ans = 0
    for num in dp[n]:
        ans = max(ans, num)
        
    return ans