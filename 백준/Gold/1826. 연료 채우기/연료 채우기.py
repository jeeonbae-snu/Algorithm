import sys
import heapq

def main():
    input = sys.stdin.readline

    N = int(input().strip())
    stations = [tuple(map(int, input().split())) for _ in range(N)]
    L, P = map(int, input().split())

    # 주유소를 거리 오름차순으로 정렬
    stations.sort()

    # 현재 연료로 도달 가능한 거리
    reach = P
    i = 0
    refuels = 0
    maxheap = []  # 파이썬 heapq는 최소힙이므로 연료를 음수로 넣어 최대힙처럼 사용

    while reach < L:
        # 현재 도달 가능한 모든 주유소를 후보에 추가
        while i < N and stations[i][0] <= reach:
            heapq.heappush(maxheap, -stations[i][1])
            i += 1

        # 더 이상 갈 수 있는 주유소가 없는데 목적지에 못 미치면 실패
        if not maxheap:
            print(-1)
            return

        # 지금까지 지나친 주유소 중 가장 많은 연료를 주는 곳에서 한 번 보충
        reach += -heapq.heappop(maxheap)
        refuels += 1

    print(refuels)

if __name__ == "__main__":
    main()
