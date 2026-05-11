# [Gold III] 소수의 연속합 (BOJ 1644)
# 분류: 수학, 정수론, 두 포인터, 소수 판정, 에라토스테네스의 체

import sys
input = sys.stdin.readline

N = int(input())
prime_list = []

is_prime = [True] * (N+1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(N**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, N+1, i):
            is_prime[j] = False
prime_list = [i for i, flag in enumerate(is_prime) if flag]

end = 0
interval_sum = 0
count = 0
n = len(prime_list)

for start in range(n):
    while end < n and interval_sum < N:
        interval_sum += prime_list[end]
        end += 1

    if interval_sum == N:
        count += 1
    interval_sum -= prime_list[start]
print(count)