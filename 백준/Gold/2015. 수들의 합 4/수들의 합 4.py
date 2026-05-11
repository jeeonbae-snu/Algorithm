import sys
from collections import defaultdict

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

freq = defaultdict(int)
freq[0] = 1  # prefix가 0인 경우(처음부터 j까지 합이 K인 경우) 카운트 위해

ans = 0
s = 0
for x in A:
    s += x
    ans += freq[s - K]
    freq[s] += 1

print(ans)
