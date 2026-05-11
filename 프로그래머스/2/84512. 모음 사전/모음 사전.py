def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    answer = 0
    base = [781, 156, 31, 6, 1]  # 각 자리의 값 (5^4 + 5^3 + 5^2 + 5^1 + 5^0)

    for i, char in enumerate(word):
        answer += vowels.index(char) * base[i] + 1
    
    return answer
