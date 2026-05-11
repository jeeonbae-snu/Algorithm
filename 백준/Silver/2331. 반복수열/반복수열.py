a, p = map(int, input().split()) # a = init_num, p = num_of_squares

def sequence(a, p, result):
    num_list = list(map(int, str(a)))
    tmp = 0
    for num in num_list:
        tmp += num ** p

    if tmp in result:
        
        return result[:result.index(tmp)]

    else:
        result.append(tmp)
        return sequence(tmp, p, result)

result = sequence(a, p, [a])   
print(len(result))