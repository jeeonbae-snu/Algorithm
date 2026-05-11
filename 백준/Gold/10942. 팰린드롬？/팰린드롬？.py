# [Gold IV] 팰린드롬? (BOJ 10942)
# 분류: 다이나믹 프로그래밍
# 접근: 2차원 DP[i][j]로 arr[i..j]가 팰린드롬인지 짧은 구간부터 채워 쿼리 O(1)에 응답


import sys
input = sys.stdin.readline

def main():
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(M)]

    # dp[i][j] = arr[i..j] 구간이 팰린드롬인지 여부
    dp = [[False] * N for _ in range(N)]

    # 길이 1: 항상 팰린드롬
    for i in range(N):
        dp[i][i] = True

    # 길이 2: 양 끝 값이 같으면 팰린드롬
    for i in range(N - 1):
        if arr[i] == arr[i+1]:
            dp[i][i+1] = True

    # 길이 3 이상
    # l은 구간의 길이
    for l in range(3, N + 1):
        for i in range(N - l + 1):
            j = i + l - 1
            # 양 끝이 같고, 안쪽(dp[i+1][j-1])도 팰린드롬이면
            if arr[i] == arr[j] and dp[i+1][j-1]:
                dp[i][j] = True

    # 쿼리 처리
    out = []
    for s, e in queries:
        # 입력은 1-based index이므로 0-based로 변환
        out.append('1' if dp[s-1][e-1] else '0')

    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()
