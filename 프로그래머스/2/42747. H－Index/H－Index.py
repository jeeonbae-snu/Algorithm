
def solution(citations):
    max_h = 0
    citations.sort(reverse = True)
    for i in range(len(citations)):
        if citations[i] > i:
            max_h += 1
        else:
            break
    return max_h