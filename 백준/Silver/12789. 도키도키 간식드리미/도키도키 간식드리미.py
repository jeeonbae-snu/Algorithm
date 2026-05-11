# [Silver III] 도키도키 간식드리미 (BOJ 12789)
# 분류: 자료 구조, 스택
# 접근: 받아야 할 다음 번호를 추적하며, 일치하지 않는 학생은 보조 스택에 쌓고 일치 시 스택 top과 연쇄적으로 처리

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
