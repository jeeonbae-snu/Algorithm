import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input().strip()
    n = int(input())
    raw = input().strip()
    if n == 0:
        arr = deque()
    else:
        arr = deque(map(int, raw[1:-1].split(',')))

    rev = False
    error = False

    for op in p:
        if op == 'R':
            rev = not rev
        else:  # op == 'D'
            if not arr:
                print("error")
                error = True
                break
            if rev:
                arr.pop()      # 뒤에서 제거
            else:
                arr.popleft()  # 앞에서 제거

    if error:
        continue

    # 출력
    if rev:
        arr.reverse()
    print("[" + ",".join(map(str, arr)) + "]")
