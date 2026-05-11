# [level 3] 단어 변환 (프로그래머스 43163)
# 분류: BFS/DFS
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

from collections import deque

def can_change(target, word):
    count = 0
    n = len(word)
    
    for i in range(n):
        if target[i] != word[i]:
            count += 1
    
    return count == 1  # 정확히 한 글자만 달라야 함

def solution(begin, target, words):
    
    if target not in words:
        return 0

    else:
        q = deque()
        words.append(begin)
        used = [False] * len(words)
        distance = [0] * len(words)
        q.append(begin) 
       
        while q:
            curr_word = q.popleft()
            if curr_word == target:
                return distance[words.index(curr_word)]
            
            for i in range(len(words)):
                next_word = words[i]
                if can_change(curr_word, next_word) and not used[i]:
                    used[i] = True
                    distance[i] = distance[words.index(curr_word)] + 1
                    q.append(next_word)
        
        return 0
