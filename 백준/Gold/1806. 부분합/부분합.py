# [Gold IV] 부분합 (BOJ 1806)
# 분류: 누적 합, 두 포인터

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
data = list(map(int, input().split()))

min_len = float('inf')
curr_sum = 0
start = 0
end = 0

while True:
    if curr_sum >= S:
        min_len = min(min_len, end - start)
        curr_sum -= data[start]
        start += 1
    else:
        if end == N:
            break
        curr_sum += data[end]
        end += 1

print(0 if min_len == float('inf') else min_len)
