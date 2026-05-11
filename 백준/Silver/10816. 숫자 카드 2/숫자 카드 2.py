# [Silver IV] 숫자 카드 2 (BOJ 10816)
# 분류: 자료 구조, 정렬, 이분 탐색, 해시를 사용한 집합과 맵
# 접근: Union-Find로 연결성을 관리하며 그룹을 합치고 대표를 찾음

import sys
input = sys.stdin.readline

def binary_search(arr, n, target):
    mid = n // 2
    start = 0
    end = n - 1
    while end >= start:
        if target == arr[mid]:
            cnt = 1
            left = mid - 1
            right = mid + 1
            while left >= 0 and arr[left] == target:
                left -= 1
                cnt += 1
            while right < n and arr[right] == target:
                right += 1
                cnt += 1
            return cnt
        elif target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
        mid = (start + end) // 2
    return 0

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))
find = {}
cards.sort()
for num in nums:
    if num not in find.keys():
        ans = binary_search(cards, N, num)
        find[num] = ans
        print(ans, end=' ')
    else:
        print(find[num], end=' ')