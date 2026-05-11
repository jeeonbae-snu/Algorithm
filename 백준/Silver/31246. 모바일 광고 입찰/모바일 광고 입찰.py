import sys
input = sys.stdin.readline
N, K = map(int, input().split())
n_list = [[int(x) for x in input().split()] for _ in range(N)]
sub = []
for n in n_list:
    sub.append(n[1] - n[0])
sub.sort()
if sub[K-1] < 0:
    print(0)
else:
    print(sub[K-1])
