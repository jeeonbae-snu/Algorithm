stack = []
k = int(input())
for _ in range(k):
    i = int(input())
    if i == 0:
        stack.pop()
    else:
        stack.append(i)
print(sum(stack))
