import sys
from math import gcd, factorial
input = sys.stdin.readline

N = int(input())
nums = [input().strip() for _ in range(N)]
K = int(input())

# 1) 각 숫자의 길이와 mod K 값 계산
lengths = [len(s) for s in nums]
remainders = []
for s in nums:
    r = 0
    for ch in s:
        r = (r * 10 + int(ch)) % K
    remainders.append(r)

# 2) 10^L mod K 테이블 채우기 (L 최대 50)
max_len = max(lengths)
pow10 = [1] * (max_len + 1)
for i in range(1, max_len + 1):
    pow10[i] = (pow10[i-1] * 10) % K

# 숫자 i를 뒤에 붙였을 때 곱해질 10^len_i mod K
pow10_len = [pow10[L] for L in lengths]

# 3) bit-mask DP
M = 1 << N
dp = [ [0] * K for _ in range(M) ]
dp[0][0] = 1

for mask in range(M):
    # mask에 포함된 숫자를 이미 모두 썼다면 스킵
    if mask == M - 1:
        continue

    for i in range(N):
        if mask & (1 << i):
            continue
        nxt = mask | (1 << i)
        add10 = pow10_len[i]
        r_i   = remainders[i]

        # 기존 상태 r에서 붙인 후의 new_r 계산
        # dp[nxt][new_r] += dp[mask][r]
        for r in range(K):
            cnt = dp[mask][r]
            if cnt:
                new_r = (r * add10 + r_i) % K
                dp[nxt][new_r] += cnt

# 4) 결과: 성공한 순열 수 / 전체 순열 수
success = dp[M-1][0]
total   = factorial(N)

# 5) 기약분수로 출력
g = gcd(success, total)
print(f"{success//g}/{total//g}")
