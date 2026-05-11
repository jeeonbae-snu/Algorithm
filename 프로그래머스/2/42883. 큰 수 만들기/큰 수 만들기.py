def solution(number, k):
    stack = []  # 최종 결과를 저장할 스택

    for num in number:
        # 스택의 마지막 숫자가 현재 숫자보다 작고, 아직 제거할 횟수(k)가 남아 있다면
        while stack and stack[-1] < num and k > 0:
            stack.pop()  # 스택의 마지막 숫자를 제거하여 숫자를 줄임
            k -= 1       # 제거할 숫자 개수를 하나 줄임
        stack.append(num)  # 현재 숫자를 스택에 추가

    # 만약 k가 아직 남아 있다면, 뒤에서부터 남은 k개 만큼 제거
    if k > 0:
        stack = stack[:-k]
    
    return ''.join(stack)  # 스택에 남은 숫자들을 문자열로 반환

# 예시 호출
print(solution("4177252841", 4))  # 예상 출력: "775841"
