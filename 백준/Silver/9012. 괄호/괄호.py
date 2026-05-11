# [Silver IV] 괄호 (BOJ 9012)
# 분류: 자료 구조, 문자열, 스택
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

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