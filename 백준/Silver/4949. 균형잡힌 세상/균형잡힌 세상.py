# [Silver IV] 균형잡힌 세상 (BOJ 4949)
# 분류: 자료 구조, 문자열, 스택
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

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