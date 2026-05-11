import re
N = int(input())
result = 0
for n in range(N):
    word = input()
    elems = "".join(set(word))
    for elem in elems:
        word = re.sub('[' + re.escape(elem) + ']+', elem, word)
    if len(elems) == len(word):
        result += 1
print(result)