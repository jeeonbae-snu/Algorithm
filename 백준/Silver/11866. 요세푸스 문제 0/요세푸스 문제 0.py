# [Silver IV] 요세푸스 문제 0 (BOJ 11866)
# 분류: 구현, 자료 구조, 큐
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

from collections import deque

N, K = map(int, input().split())
q = deque([x for x in range(1, N+1)])
pointer = K - 1
result = []
print("<", end='')

while True:
    value = q[pointer]
    if len(q) == 1:
        print(f'{value}>')
        break
    else:
        print(f'{value}, ', end='')
        q.remove(value)
        pointer = (pointer + K - 1) % len(q)