# [Gold IV] DSLR (BOJ 9019)
# 분류: 그래프 이론, 그래프 탐색, 너비 우선 탐색, 역추적
# 접근: 큐/스택으로 그래프(또는 격자)를 순회하며 조건 검사

from collections import deque

def bfs(start, target):
    visited = {start}
    q = deque([start])
    parent = {}
    path = []

    while q:
        n = q.popleft()

        if n == target:
            break

        d = (n * 2) % 10000
        if d not in visited:
            q.append(d)
            visited.add(d)
            parent[d] = (n, 'D')

        s = (n + 9999) % 10000
        if s not in visited:
            q.append(s)
            visited.add(s)
            parent[s] = (n, 'S')

        n2str = str(n)
        len_str = len(n2str)
        if len_str != 4:
            n2str = str(0) * (4 - len_str) + n2str

        new_l = n2str[1:] + n2str[0]
        l = int(new_l)
        if l not in visited:
            q.append(l)
            visited.add(l)
            parent[l] = (n, 'L')

        new_r = n2str[-1] + n2str[:-1]
        r = int(new_r)
        if r not in visited:
            q.append(r)
            visited.add(r)
            parent[r] = (n, 'R')

    prev = target
    while True:
        path.append(parent[prev][1])
        prev = parent[prev][0]
        if prev == start:
            break

    return path[::-1]

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    path = bfs(A, B)
    print(''.join((path)))