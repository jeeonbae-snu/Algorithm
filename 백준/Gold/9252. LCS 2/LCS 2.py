from typing import Tuple

def lcs(a: str, b: str) -> Tuple[int, str]:
    """
    문자열 a, b 의 최장 공통 부분 수열(LCS)의 길이와
    그 중 하나의 실제 수열을 반환한다.
    시간 복잡도: O(N*M)
    공간 복잡도: O(N*M)
    """
    n, m = len(a), len(b)
    # dp[i][j]: a[:i]와 b[:j]의 LCS 길이
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # 1) DP 테이블 채우기
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # 2) 역추적하여 하나의 LCS 수열 복원
    i, j = n, m
    lcs_chars = []
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            lcs_chars.append(a[i-1])
            i -= 1; j -= 1
        elif dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    lcs_seq = ''.join(reversed(lcs_chars))
    return dp[n][m], lcs_seq

if __name__ == "__main__":
    A = input()
    B = input()
    length, seq = lcs(A, B)
    print(length)
    print(seq)
