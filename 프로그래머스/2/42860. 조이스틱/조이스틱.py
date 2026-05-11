# [level 2] 조이스틱 (프로그래머스 42860)

    

#     ans += len(name) - 1 # 문자위치 이동
    
#     return ans
def solution(name):
    ans = 0
    length = len(name)
    
    # 변경 비용 계산
    for char in name:
        ans += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
    
    # 좌우 이동 비용 계산
    move = length - 1
    for i in range(length):
        next_i = i + 1
        while next_i < length and name[next_i] == 'A':
            next_i += 1
        move = min(move, 2 * i + length - next_i, i + 2 * (length - next_i))
    
    ans += move
    return ans

# 예시 호출
