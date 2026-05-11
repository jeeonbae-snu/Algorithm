import sys, heapq
input = sys.stdin.readline

N = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(N)]  # (d, l)
jobs.sort(key=lambda x: x[0])  # 마감 오름차순

heap = []  # 선택한 작업들의 이익(최소힙)
for d, l in jobs:
    heapq.heappush(heap, l)   # 일단 넣고
    if len(heap) > d:         # 마감 d까지는 d개까지만 가능(시간 0..d-1)
        heapq.heappop(heap)   # 가장 이익 작은 작업을 버림

print(sum(heap))