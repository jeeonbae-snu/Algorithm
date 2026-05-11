import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    nums = list(map(lambda x: int(x)-1, input().split()))

    visited = [0] * n
    team_cnt = 0

    for i in range(n):
        if visited[i]:
            continue

        start = i
        cur = i
        # 현재 탐색 ID로 표시해두면, 같은 ID로 다시 나오면 사이클
        while visited[cur] == 0:
            visited[cur] = start + 1
            cur = nums[cur]

        # 사이클이 맞다면
        if visited[cur] == start + 1:
            # cur부터 출발해 한 바퀴 돌며 개수 계산
            node = nums[cur]
            cnt = 1
            while node != cur:
                cnt += 1
                node = nums[node]
            team_cnt += cnt

    # 팀(사이클)에 속하지 않은 사람 수
    print(n - team_cnt)