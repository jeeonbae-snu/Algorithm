import sys
input = sys.stdin.readline

def min_merge_cost(sizes):
    """
    sizes: 합칠 파일들의 크기 리스트 (1차원, 0-indexed)
    반환값: 최소 합병 비용
    """
    n = len(sizes)
    # prefix_sum[i] = sizes[0] + ... + sizes[i-1]
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + sizes[i]
    # sum_range(i,j) = prefix_sum[j+1] - prefix_sum[i]
    def sum_range(i, j):
        return prefix_sum[j+1] - prefix_sum[i]

    # dp[i][j]: i~j 구간을 하나로 합칠 때 최소 비용
    dp = [[0] * n for _ in range(n)]
    # opt[i][j]: dp[i][j]를 달성하는 k의 최적 분할점 (Knuth 최적화용)
    opt = [[0] * n for _ in range(n)]
    for i in range(n-1):
        dp[i][i+1] = sizes[i] + sizes[i+1]
        opt[i][i+1] = i

    # 구간 길이 L = 2부터 n-1까지
    for L in range(2, n):
        for i in range(n-L):
            j = i + L
            # Knuth 조건: opt[i][j-1] ≤ opt[i][j] ≤ opt[i+1][j]
            lo = opt[i][j-1]
            hi = opt[i+1][j]
            best_cost = float('inf')
            best_k = lo
            total = sum_range(i, j)
            # k를 [lo..hi] 까지만 탐색
            for k in range(lo, hi+1):
                cost = dp[i][k] + dp[k+1][j] + total
                if cost < best_cost:
                    best_cost = cost
                    best_k = k
            dp[i][j] = best_cost
            opt[i][j] = best_k

    return dp[0][n-1]

def main():
    T = int(input())
    for _ in range(T):
        K = int(input())
        sizes = list(map(int, input().split()))
        print(min_merge_cost(sizes))

if __name__ == "__main__":
    main()
