# [level 2] 더 맵게 (프로그래머스 42626)
# 분류: 힙(우선순위 큐)
# 접근: 최소힙에서 가장 작은 두 음식을 꺼내 first + 2×second 로 합쳐 다시 push, 모두 K 이상이면 종료



import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  # 주어진 리스트를 힙 구조로 변환
    ans = 0

    while scoville[0] < K:  # 최소 스코빌이 K보다 작은 동안 반복
        if len(scoville) < 2:  # 트리거가 부족한 경우
            return -1

        # 두 개의 최소 스코빌 값을 꺼냄
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        # 새로운 스코빌 지수를 계산하고 다시 삽입
        new_scoville = first + 2 * second
        heapq.heappush(scoville, new_scoville)

        ans += 1  # 스코빌 지수를 만들 때마다 카운트 증가

    return ans

print(solution([1, 2, 3, 9, 10, 12], 7))  # 결과: 2
