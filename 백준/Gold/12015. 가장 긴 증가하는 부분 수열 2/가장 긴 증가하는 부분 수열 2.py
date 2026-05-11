import sys
import bisect
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# LIS 배열 (실제 수열은 아니고, 길이 계산용)
lis = []

for num in A:
    # lis에서 num이 들어갈 위치를 이진탐색
    idx = bisect.bisect_left(lis, num)
    
    if idx == len(lis):
        lis.append(num)
    else:
        lis[idx] = num

print(len(lis))
