# [Gold III] 오등큰수 (BOJ 17299)
# 분류: 자료 구조, 스택
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))

cnt_dict = {}
res = [-1] * N
stack = []

for v in seq:
    if v in cnt_dict.keys():
        cnt_dict[v] += 1
    else:
        cnt_dict[v] = 1

for i, v in enumerate(seq):
    while stack and cnt_dict[seq[stack[-1]]] < cnt_dict[v]:
        idx = stack.pop()
        res[idx] = v
    stack.append(i)

print(*res)

