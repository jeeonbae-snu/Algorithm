# [level 2] 타겟 넘버 (프로그래머스 43165)
# 분류: 백트래킹
# 접근: 선택/해제를 반복하며 가능한 모든 경우 탐색

from itertools import combinations

def solution(numbers, target):
    n = len(numbers)
    count = 0
    for i in range(n):
        num_plus = n - i
        num_minus = i
        tmp = 0
        seq_list = [x for x in range(n)]
        for positions in combinations(seq_list, i):
            for position in positions:
                tmp -= numbers[position]
                seq_list.remove(position)
            for position in seq_list:
                tmp += numbers[position]
            if tmp == target:
                count += 1
            tmp = 0
            seq_list = [x for x in range(n)]
    return count