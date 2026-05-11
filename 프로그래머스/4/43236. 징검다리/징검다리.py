# [level 4] 징검다리 (프로그래머스 43236)
# 분류: 이분탐색, 백트래킹, 투포인터
# 접근: 정렬된 공간에서 좌우를 좁혀가며 조건을 만족하는 값 탐색


    

def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    
    left, right = 0, distance
    ans = 0
    
    while left <= right:
        
        mid = (left + right) // 2
        prev = 0
        removed = 0
        
        for rock in rocks:
            if rock - prev < mid:
                removed += 1
            else:
                prev = rock
        
        if removed > n:
            right = mid - 1
        else:
            left = mid + 1
            ans = mid
            
    return ans

