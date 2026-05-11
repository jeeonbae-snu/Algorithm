import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
x = int(input())

# 리스트가 정렬되어 있지 않은 경우 정렬
data.sort()

count = 0
left, right = 0, n - 1

while left < right:
    current_sum = data[left] + data[right]
    if current_sum == x:
        # 만약 같은 값이 여러 개 있다면 같은 그룹으로 처리해야 하는 경우,
        # 두 값이 다르면 각각 중복된 개수를 고려해 계산하고 포인터들을 이동합니다.
        # 여기서는 단순히 쌍 하나씩만 카운트하는 경우:
        count += 1
        left += 1
        right -= 1
    elif current_sum < x:
        left += 1
    else:
        right -= 1

print(count)
