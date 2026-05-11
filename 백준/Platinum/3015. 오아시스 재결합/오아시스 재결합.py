import sys
input = sys.stdin.readline

n = int(input())
heights = [int(input()) for _ in range(n)]

stack = []
result = 0

for h in heights:
    cnt = 1

    # 현재 사람보다 키가 작거나 같은 사람 pop
    while stack and stack[-1][0] <= h:
        height, count = stack.pop()
        result += count
        if height == h:
            cnt += count

    # 현재 사람과 남아있는 사람 중 가장 가까운 사람 1명은 볼 수 있음
    if stack:
        result += 1

    stack.append((h, cnt))

print(result)
