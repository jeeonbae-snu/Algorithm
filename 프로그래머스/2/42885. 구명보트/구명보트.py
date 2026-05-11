def solution(people, limit): 
    answer = 0
    people.sort()
    start = 0
    end = 1
    while( (start + end)  <= len(people) ):
        if (people[start] + people[-end]) > limit:
            end += 1
        else:
            start += 1
            end += 1    
        answer +=1
    return answer