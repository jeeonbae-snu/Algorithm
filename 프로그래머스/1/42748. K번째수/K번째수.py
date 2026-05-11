def solution(array, commands):
    tmp = []
    for command in commands:
        tmp.append(sorted(array[command[0] - 1 : command[1]])[command[2]-1])
    return tmp