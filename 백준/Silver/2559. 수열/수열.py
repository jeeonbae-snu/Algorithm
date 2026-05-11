# [Silver III] 수열 (BOJ 2559)
# 분류: 누적 합, 두 포인터, 슬라이딩 윈도우

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temperature = list(map(int, input().split()))

ans = [-1e9] * N
prefix_sum_list = [0] * N
prefix_sum = 0

for i in range(N):
    prefix_sum += temperature[i]
    prefix_sum_list[i] = prefix_sum
    if i < K - 1:
        continue
    elif i == K - 1:
        ans[i] = prefix_sum_list[i]
    else:
        ans[i] = prefix_sum_list[i] - prefix_sum_list[i-K]

print(max(ans))
