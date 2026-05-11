# [Gold V] 치킨 배달 (BOJ 15686)
# 분류: 구현, 브루트포스 알고리즘, 백트래킹
# 접근: 선택/해제를 반복하며 가능한 모든 경우 탐색

import sys
from itertools import combinations

input = sys.stdin.readline

def calculate_distance(houses, chickens):
    total_dist = 0
    for hx, hy in houses:
        min_dist = float('inf')
        for cx, cy in chickens:
            dist = abs(hx - cx) + abs(hy - cy)
            min_dist = min(min_dist, dist)
        total_dist += min_dist
    return total_dist

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((j, i))
        elif city[i][j] == 2:
            chickens.append((j, i))

min_distance = float('inf')
for comb in combinations(chickens, M):
    dist = calculate_distance(houses, comb)
    min_distance = min(min_distance, dist)

print(min_distance)