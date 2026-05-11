import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n_list = list(map(int, input().split()))
mod_list = [0] * M
temp = 0

for i in range(N):
    temp += n_list[i]
    mod_list[temp % M] += 1

ans = mod_list[0]
for j in range(M):
    ans += mod_list[j] * (mod_list[j] - 1) // 2
print(ans)
