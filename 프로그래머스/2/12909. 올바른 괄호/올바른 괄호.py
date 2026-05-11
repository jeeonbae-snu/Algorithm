# [level 2] 올바른 괄호 (프로그래머스 12909)
# 분류: 스택, 큐
# 접근: 길이가 홀수면 즉시 False, 그 외 스택으로 () 짝맞춤 검사

def solution(s):
    # 길이가 홀수인 경우는 무조건 False
    if len(s) % 2 != 0:
        return False
    
    # 스택을 사용하여 괄호 쌍을 체크
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)  # 열린 괄호를 스택에 추가
        elif char == ')':
            if not stack:
                return False  # 닫힌 괄호가 있지만 열린 괄호가 없음
            stack.pop()  # 열린 괄호와 쌍을 이루므로 제거

    return len(stack) == 0  # 스택이 비어있다면 괄호가 모두 쌍을 이룬 것

