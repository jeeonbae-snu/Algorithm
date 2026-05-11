# [Silver V] 집합 (BOJ 11723)
# 분류: 구현, 집합과 맵, 비트마스킹

import sys
input = sys.stdin.readline

M = int(input())
S = 0

for _ in range(M):
    parts = input().split()
    op = parts[0]

    if op == 'add':
        x = int(parts[1]) - 1
        S |= (1 << x)
    elif op == 'remove':
        x = int(parts[1]) - 1
        S &= ~(1 << x)
    elif op == 'check':
        x = int(parts[1]) - 1
        sys.stdout.write('1\n' if (S & (1 << x)) else '0\n')
    elif op == 'toggle':
        x = int(parts[1]) - 1
        S ^= (1 << x)
    elif op == 'all':
        S = (1 << 20) - 1
    elif op == 'empty':
        S = 0
