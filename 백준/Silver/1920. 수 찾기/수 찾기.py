# [Silver IV] 수 찾기 (BOJ 1920)
# 분류: 자료 구조, 정렬, 이분 탐색, 집합과 맵, 해시를 사용한 집합과 맵
# 접근: Union-Find로 연결성을 관리하며 그룹을 합치고 대표를 찾음

def binary_search(arr, n, target):
    mid = n // 2
    start = 0
    end = n - 1
    while end >= start:
        if target == arr[mid]:
            return 1
        elif target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
        mid = (start + end) // 2
    return 0

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
find = list(map(int, input().split()))

for num in find:
    print(binary_search(arr, n, num))