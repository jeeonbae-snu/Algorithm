import sys

input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
data.sort()

start, end = 0, N - 1
min_diff = float('inf')
s1, s2 = 0, 0

while start < end:
    current_sum = data[start] + data[end]
    diff = abs(current_sum)

    if diff < min_diff:
        min_diff = diff
        s1, s2 = data[start], data[end]

    if current_sum < 0:
        start += 1  # 합이 음수라면 왼쪽 값을 증가시켜 합을 증가
    elif current_sum > 0:
        end -= 1  # 합이 양수라면 오른쪽 값을 감소시켜 합을 감소
    else:
        # 합이 정확히 0인 경우, 더 이상 개선할 수 없으므로 반복 종료
        break

print(s1, s2)
