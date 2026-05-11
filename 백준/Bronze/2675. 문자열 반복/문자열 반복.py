t = int(input())
for _ in range(t):
    n, s = input().split()
    for c in s:
        for i in range(int(n)):
            print(c, end ='')
    print()