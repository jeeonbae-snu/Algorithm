# [Gold II] 레이스 (BOJ 1508)
# 분류: 그리디 알고리즘, 이분 탐색, 매개 변수 탐색, 역추적
# 접근: 정렬된 공간에서 좌우를 좁혀가며 조건을 만족하는 값 탐색

def binary_search(pos, M):
    low, high = 0, pos[-1] - pos[0]

    while low < high:
        mid = (low + high + 1) // 2

        if can(mid, pos, M):
            low = mid
        else:
            high = mid - 1

    return low

def can(d, pos, M):
    cnt = 0
    last = -1e9

    for x in pos:
        if x >= last + d:
            cnt += 1
            last = x
            if cnt >= M:
                return True

    return False

N, M, K = map(int, input().split())
pos = list(map(int, input().split()))

min_max_gap = binary_search(pos, M)
ans = [0] * K
last = -1e9
cnt = 0

for i, x in enumerate(pos):
    if x >= last + min_max_gap:
        last = x
        cnt += 1
        ans[i] = 1
    if cnt == M:
        break

print(''.join(map(str, ans)))

