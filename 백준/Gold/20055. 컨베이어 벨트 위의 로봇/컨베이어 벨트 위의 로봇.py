N, K = map(int, input().split())
arr = list(map(int, input().split()))
robots = [False] * N  # 로봇은 0 ~ N-1 위치에만 존재
cnt = 0  # 로봇 순서
level = 1

while True:
    # 1. 벨트와 로봇 회전
    arr = arr[-1:] + arr[:-1]
    robots = robots[-1:] + robots[:-1]
    if robots[N-1]:  # 내리는 위치에 로봇이 있으면 제거
        robots[N-1] = False

    # 2. 로봇 이동 (오른쪽에서 왼쪽으로, 먼저 올라간 순서대로)
    for i in range(N-2, -1, -1):
        if robots[i] and not robots[i+1] and arr[i+1] > 0:
            robots[i] = False
            robots[i+1] = True
            arr[i+1] -= 1
    if robots[N-1]:  # 내리는 위치에 로봇이 있으면 제거
        robots[N-1] = False

    # 3. 로봇 올리기
    if arr[0] > 0:
        robots[0] = True
        arr[0] -= 1

    # 4. 종료 조건
    if arr.count(0) >= K:
        break

    level += 1

print(level)