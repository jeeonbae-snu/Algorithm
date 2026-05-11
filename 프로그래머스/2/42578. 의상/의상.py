from functools import reduce

def solution(clothes):
    clothes_type = {}
    
    # 의상 종류별로 의상 이름을 리스트에 저장
    for cloth in clothes:
        if cloth[1] not in clothes_type:
            clothes_type[cloth[1]] = [cloth[0]]
        else:
            clothes_type[cloth[1]].append(cloth[0])

    # 각 의상 종류별로 (입을 수 있는 개수 + 1) 을 계산
    lengths = [len(value) + 1 for value in clothes_type.values()]

    # 모든 의상 종류의 개수를 곱한 뒤 아무것도 입지 않는 경우(1)를 빼줌
    result = reduce(lambda x, y: x * y, lengths) - 1

    return result
