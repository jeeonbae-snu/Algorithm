from collections import deque

def solution(arr):
    q = deque()
    prev = -1

    for i, elem in enumerate(arr):
        if i == 0:
            q.append(elem)
            prev = elem
        else:
            if prev != elem:
                q.append(elem)
                prev = elem

    return list(q)

print(solution([1,1,3,3,0,1,1]))