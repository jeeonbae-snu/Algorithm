# [Silver IV] 스택 2 (BOJ 28278)
# 분류: 자료 구조, 스택
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

import sys
input = sys.stdin.readline

stack = []
N = int(input()) #명령의 수
for _ in range(N):
    command = list(map(int, input().split()))

    if command[0] == 1:
        stack.append(command[1])

    elif command[0] == 2:
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)

    elif command[0] == 3:
        print(len(stack))

    elif command[0] == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == 5:
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
