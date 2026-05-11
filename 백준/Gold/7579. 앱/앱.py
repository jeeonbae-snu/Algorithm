import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mems = list(map(int, input().split()))
costs = list(map(int, input().split()))

sum_cost = sum(costs)
INF = -10**18  # 최대 메모리 구하기 위해 음의 무한대

# 1) 메모리 기준 상태 개수 = M+1
# 2) 비용 기준 상태 개수 = sum_cost+1
if M <= sum_cost:
    # (A) 메모리 기준 DP: dp[j] = min 비용
    dp = [10**18] * (M+1)
    dp[0] = 0
    for w, v in zip(mems, costs):
        for j in range(M, -1, -1):
            if dp[j] == 10**18: continue
            nxt = min(M, j + w)
            dp[nxt] = min(dp[nxt], dp[j] + v)
    print(dp[M])

else:
    # (B) 비용 기준 DP: dp_cost[c] = max 메모리
    dp_cost = [INF] * (sum_cost + 1)
    dp_cost[0] = 0
    for w, v in zip(mems, costs):
        # 비용을 뒤→앞으로 순회하며 0/1 knapsack
        for c in range(sum_cost, v-1, -1):
            if dp_cost[c-v] >= 0:
                candidate = dp_cost[c-v] + w
                if candidate > dp_cost[c]:
                    dp_cost[c] = candidate

    # 최소 비용 찾기
    for c in range(sum_cost+1):
        if dp_cost[c] >= M:
            print(c)
            break
