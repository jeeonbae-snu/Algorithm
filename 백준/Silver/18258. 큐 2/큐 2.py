# [Silver IV] 큐 2 (BOJ 18258)
# 분류: 자료 구조, 큐
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
q = deque()

for _  in range(N):
    command = input().split()

    if command[0] == 'push':
        q.append(command[1])

    elif command[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)

    elif command[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)   

    elif command[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)

    elif command[0] == 'size':
        print(len(q))

    elif command[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)

