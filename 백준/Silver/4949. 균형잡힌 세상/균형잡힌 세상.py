# [Silver IV] 균형잡힌 세상 (BOJ 4949)
# 분류: 자료 구조, 문자열, 스택
# 접근: 스택으로 (), [] 짝맞춤 검사 — 닫는 괄호에서 top과 종류 비교, 마지막에 스택이 비어야 균형

while True:
    stack = []
    string = input()
    is_balance = True

    if string == '.':
        break

    for char in string:
        if char == '(' or char == '[':
            stack.append(char)

        elif char == ')':
            if len(stack):
                pop_char = stack.pop()
                if pop_char != '(':
                    is_balance = False
                    break
            else:
                is_balance = False
                break

        elif char == ']':
            if len(stack):
                pop_char = stack.pop()
                if pop_char != '[':
                    is_balance = False
                    break
            else:
                is_balance = False
                break
                
    if is_balance and not stack:
        print('yes')
    else:
        print('no')