import heapq
import sys
N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    item = int(sys.stdin.readline())
    if item > 0:
        heapq.heappush(heap, item)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
