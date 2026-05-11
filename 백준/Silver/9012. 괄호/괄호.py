# [Silver IV] 괄호 (BOJ 9012)
# 분류: 자료 구조, 문자열, 스택
# 접근: 스택으로 () 짝맞춤 — 빈 스택에 ")" 오거나 끝에 스택이 남으면 NO

T = int(input())
for _ in range(T):
    string = input()
    stack = []
    flag = False
    for char in string:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if len(stack) <= 0:
                print('NO')
                flag = True
                break
            else:
                stack.pop()
    if flag:
        continue
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')