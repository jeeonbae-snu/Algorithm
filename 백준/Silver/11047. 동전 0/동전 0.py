# [Silver IV] 동전 0 (BOJ 11047)
# 분류: 그리디 알고리즘

N, K = map(int, input().split())
coins = []

for i in range(N):
    coins.append(int(input()))

i = N - 1
ans = 0

while True:
    quotient = K // coins[i]

    if quotient > 0:
        K -= quotient * coins[i]
        ans += quotient

    if K == 0:
        break

    i -= 1

print(ans)