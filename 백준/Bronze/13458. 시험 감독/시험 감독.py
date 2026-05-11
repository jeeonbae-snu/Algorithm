N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
temp = []

for i in range(N):
    remaining = A[i] - B 
    if remaining <= 0:    
        temp.append(0)
    else:              
        if remaining % C == 0:
            temp.append(remaining // C)
        else:
            temp.append(remaining // C + 1)

print(len(A) + sum(temp))