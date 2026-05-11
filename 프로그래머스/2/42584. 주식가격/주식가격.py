def solution(prices):
    n = len(prices)
    answer = [0] * n

    stack = []  # 주가가 아직 떨어지지 않은 시점들을 쌓아둘 스택

    # 1) 모든 시점을 순회
    for i in range(n):
        # 스택이 비어있지 않고, 현재 주가가 스택 top의 주가보다 < (떨어졌다) 면
        # top에 있던 시점의 '떨어지지 않은 기간'을 계산하고 pop
        while stack and prices[stack[-1]] > prices[i]:
            top = stack.pop()
            answer[top] = i - top  # 떨어지기까지 걸린 시간
            
        # 현재 시점을 스택에 넣기
        stack.append(i)
    
    # 2) 순회가 끝나고도 스택에 남아 있는 시점 처리
    #    => 끝까지 떨어지지 않은 것
    while stack:
        top = stack.pop()
        answer[top] = (n - 1) - top

    return answer
