import sys
input = sys.stdin.readline
N, M = map(int, input().split())
n_list = list(map(int, input().split()))
total_sum = [0] * (N+1)
temp = 0
for i, n in enumerate(n_list):
    temp += n
    total_sum[i+1] = temp

for _ in range(M):
    start, end = map(int, input().split())
    print(total_sum[end] - total_sum[start-1])