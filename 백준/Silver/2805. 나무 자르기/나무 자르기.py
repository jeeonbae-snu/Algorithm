# [Silver II] 나무 자르기 (BOJ 2805)
# 분류: 이분 탐색, 매개 변수 탐색
# 접근: 정렬된 공간에서 좌우를 좁혀가며 조건을 만족하는 값 탐색

def binary_search(arr, M):
    start, end = 1, max(arr)
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        tree = sum([x - min(mid, x) for x in arr])

        if tree >= M:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer

N, M = map(int, input().split())
heights = list(map(int, input().split()))
print(binary_search(heights, M))
