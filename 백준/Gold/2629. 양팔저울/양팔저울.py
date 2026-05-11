import sys
input = sys.stdin.readline

def main():
    n = int(input())
    weights = list(map(int, input().split()))
    m = int(input())
    targets = list(map(int, input().split()))

    total = sum(weights)
    # dp[x] = True 면, 한쪽 저울에 올려볼 수 있는 무게 xg
    dp = [False] * (total + 1)
    dp[0] = True  # 아무것도 올리지 않았을 때 0g은 당연히 가능

    # 각 추마다 가능한 무게 집합을 전파
    for w in weights:
        next_dp = dp[:]  # 이전 상태 복사
        for curr_w, reachable in enumerate(dp):
            if not reachable:
                continue
            # 1) 이 추를 오른쪽 저울에 올리기: curr_w + w
            if curr_w + w <= total:
                next_dp[curr_w + w] = True
            # 2) 이 추를 왼쪽 저울에 올리기 (차이 계산): |curr_w - w|
            diff = abs(curr_w - w)
            next_dp[diff] = True
        dp = next_dp

    # 결과 출력
    # 측정하려는 각 무게 t에 대해, dp[t]가 True이면 Y, 아니면 N
    answer = []
    for t in targets:
        if t <= total and dp[t]:
            answer.append("Y")
        else:
            answer.append("N")

    print(" ".join(answer))

if __name__ == "__main__":
    main()
