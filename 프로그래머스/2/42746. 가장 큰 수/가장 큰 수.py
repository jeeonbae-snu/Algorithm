# [level 2] 가장 큰 수 (프로그래머스 42746)
# 분류: 백트래킹
# 접근: 선택/해제를 반복하며 가능한 모든 경우 탐색



from functools import cmp_to_key

def compare(a, b):
    # 두 숫자를 번갈아 붙여서 비교하여 내림차순 정렬
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0

def solution(numbers):
    # 숫자를 문자열로 변환
    str_num = list(map(str, numbers))
    # 커스텀 정렬을 통해 숫자를 최대 숫자로 나열
    str_num.sort(key=cmp_to_key(compare))
    # 정렬 결과를 합친 뒤, 결과가 0으로 시작할 경우 0 반환
    result = ''.join(str_num)
    return result if result[0] != '0' else '0'