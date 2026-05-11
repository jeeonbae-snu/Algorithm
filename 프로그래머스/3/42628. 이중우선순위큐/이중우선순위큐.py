# [level 3] 이중우선순위큐 (프로그래머스 42628)
# 분류: BFS/DFS
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

def solution(operations):
    queue = []
    for operation in operations:
        if operation[0] == "I":
            queue.append(int(operation[2:]))
            queue.sort()
        else:
            if (len(queue) !=0):
                if operation[2] =="1": #최댓값 삭제
                    del(queue[-1])
                else: #최솟값 삭제
                    del(queue[0])
    if len(queue) !=0 :
        return [queue[-1], queue[0]]
    else:
        return [0,0]