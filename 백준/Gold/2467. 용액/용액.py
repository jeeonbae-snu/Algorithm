# [Gold V] 용액 (BOJ 2467)
# 분류: 이분 탐색, 두 포인터

N = int(input())
F = list(map(int, input().split()))

INF = 2_000_000_000
best_sum = INF
best_pair = (0, 0)

s, e = 0, N - 1

while s < e:
    total = F[s] + F[e]

    if abs(total) < abs(best_sum):
        best_sum = total
        best_pair = (F[s], F[e])

    if total > 0:
        e -= 1
    else:
        s += 1

print(best_pair[0], best_pair[1])

