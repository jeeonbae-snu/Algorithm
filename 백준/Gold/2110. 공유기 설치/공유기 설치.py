# [Gold IV] 공유기 설치 (BOJ 2110)
# 분류: 이분 탐색, 매개 변수 탐색

import sys
input = sys.stdin.readline

def can_place(houses, C, d):
    count = 1
    last_pos = houses[0]
    for pos in houses[1:]:
        if pos - last_pos >= d:
            count += 1
            last_pos = pos
            if count >= C:
                return True
    return False

def max_min_distance(houses, C):
    low, high = 1, houses[-1] - houses[0]
    answer = 0

    while low <= high:
        mid = (low + high) // 2
        if can_place(houses, C, mid):
            answer = mid
            low = mid + 1
        else:
            high = mid - 1
    return answer

N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()
print(max_min_distance(houses , C))