# [Silver IV] 스택 2 (BOJ 28278)
# 분류: 자료 구조, 스택
# 접근: 리스트로 스택을 구현해 push/pop/size/empty/top 다섯 명령을 O(1)에 처리

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
