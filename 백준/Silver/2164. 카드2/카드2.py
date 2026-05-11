import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
q = deque([x for x in range(1, N+1)])

while True:
    if len(q) == 1:
        break

    q.popleft()
    q.append(q.popleft())

print(q[0])