# 배수만큼 점수를 얻고 약수많큼 점수를 잃는 게임

import sys
import math
from collections import Counter

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))

freq = Counter(nums)
max_v = max(nums)

mult_count = {}
for x, f in freq.items():
    cnt = 0
    for y in  range(x, max_v + 1, x):
        cnt += freq.get(y, 0)
    mult_count[x] = cnt - f

div_count = {}
for x, f in freq.items():
    cnt = 0
    root = int(math.isqrt(x))
    for d in range(1, root + 1):
        if x % d == 0:
            cnt += freq.get(d, 0)
            other = x // d
            if other != d:
                cnt += freq.get(other, 0)

    div_count[x] = cnt - f

res = []
for v in nums:
    res.append(mult_count[v] - div_count[v])

print(*res)