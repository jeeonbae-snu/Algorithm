# [Silver IV] 덱 2 (BOJ 28279)
# 분류: 자료 구조, 덱
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())  # 명령의 개수 입력
q = deque()  # 한 번만 생성하여 유지

for _ in range(N):
    command = list(map(int, input().split()))

    if command[0] == 1:  # 정수 x를 덱의 앞에 추가
        q.appendleft(command[1])

    elif command[0] == 2:  # 정수 x를 덱의 뒤에 추가
        q.append(command[1])

    elif command[0] == 3:  # 덱의 앞에서 원소 제거 후 출력
        print(q.popleft() if q else -1)

    elif command[0] == 4:  # 덱의 뒤에서 원소 제거 후 출력
        print(q.pop() if q else -1)

    elif command[0] == 5:  # 덱의 크기 출력
        print(len(q))

    elif command[0] == 6:  # 덱이 비어있는지 확인
        print(1 if not q else 0)

    elif command[0] == 7:  # 덱의 앞 원소 출력
        print(q[0] if q else -1)

    elif command[0] == 8:  # 덱의 뒤 원소 출력
        print(q[-1] if q else -1)
