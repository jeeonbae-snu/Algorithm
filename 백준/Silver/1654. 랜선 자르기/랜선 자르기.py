# [Silver II] 랜선 자르기 (BOJ 1654)
# 분류: 이분 탐색, 매개 변수 탐색
# 접근: 정렬된 공간에서 좌우를 좁혀가며 조건을 만족하는 값 탐색

def binary_search(arr, N):
    start, end = 1, max(arr)    
    answer = 0                   

    while start <= end:
        mid = (start + end) // 2
        count = sum(x // mid for x in arr)

        if count >= N:         
            answer = mid         
            start = mid + 1     
        else:
            end = mid - 1       

    return answer              

K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]
print(binary_search(lans, N))
