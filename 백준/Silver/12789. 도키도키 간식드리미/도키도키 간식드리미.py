# [Silver III] 도키도키 간식드리미 (BOJ 12789)
# 분류: 자료 구조, 스택
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

stack = []
count = 1

for number in n_list:
    if count == number:
         count += 1
         while stack and stack[-1] == count:
             stack.pop()
             count += 1
    else:
        stack.append(number)

if count == n + 1:
    print("Nice")
else:
    print("Sad")
