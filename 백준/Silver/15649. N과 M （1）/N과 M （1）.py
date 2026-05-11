def permutations(m, new_arr):

    if len(new_arr) == m:
        print(*new_arr)
        return

    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = 1
            permutations(m, new_arr + [arr[i]])
            visited[i] = 0

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
visited = [0] * len(arr)
permutations(M, [])