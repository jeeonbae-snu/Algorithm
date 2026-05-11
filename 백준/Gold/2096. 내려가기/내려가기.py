# [Gold V] 내려가기 (BOJ 2096)
# 분류: 다이나믹 프로그래밍, 슬라이딩 윈도우

import sys
input = sys.stdin.readline

N = int(input())
a0, a1, a2 = map(int, input().split())

max0, max1, max2 = a0, a1, a2
min0, min1, min2 = a0, a1, a2

for _ in range(N - 1):
    b0, b1, b2 = map(int, input().split())
    nmax0 = max(max0, max1) + b0
    nmax1 = max(max0, max1, max2) + b1
    nmax2 = max(max1, max2) + b2

    nmin0 = min(min0, min1) + b0
    nmin1 = min(min0, min1, min2) + b1
    nmin2 = min(min1, min2) + b2

    max0, max1, max2 = nmax0, nmax1, nmax2
    min0, min1, min2 = nmin0, nmin1, nmin2

print(max(max0, max1, max2), min(min0, min1, min2))
