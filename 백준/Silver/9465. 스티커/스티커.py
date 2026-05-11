import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    top = list(map(int, input().split()))
    bot = list(map(int, input().split()))
    if n == 1:
        print(max(top[0], bot[0]))
        continue
    # dpTop, dpBot는 각각 i열에서 해당 스티커를 선택한 최대합
    dpTop0, dpBot0 = top[0], bot[0]

    # i = 1 초기화
    dpTop1 = top[1] + dpBot0
    dpBot1 = bot[1] + dpTop0

    for i in range(2, n):
        newTop = top[i] + max(dpBot1, dpTop0, dpBot0)
        newBot = bot[i] + max(dpTop1, dpTop0, dpBot0)
        dpTop0, dpBot0, dpTop1, dpBot1 = dpTop1, dpBot1, newTop, newBot

    print(max(dpTop1, dpBot1))
