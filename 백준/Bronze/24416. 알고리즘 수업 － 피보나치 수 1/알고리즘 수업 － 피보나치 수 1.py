def count_fibo_recur(n):
    """
    재귀방식으로 피보나치 수를 계산할 때,
    기저 조건(n==1 또는 n==2) 호출 횟수를 반환합니다.
    (실제로 모든 재귀호출을 수행하면 지수 시간이 걸리므로,
    동일한 점화식을 이용하여 O(n)으로 계산합니다.)
    """
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1  # fibo(1)과 fibo(2)
    for i in range(3, n + 1):
        a, b = b, a + b
    return b

def count_fibo_dp(n):
    """
    동적 계획법을 이용할 때,
    반복문이 몇 번 실행되는지(즉, dp_count)를 반환합니다.
    n이 1 또는 2인 경우에는 반복문이 실행되지 않으므로 0을 반환합니다.
    """
    return 0 if n <= 2 else n - 2

# 입력 및 결과 출력
n = int(input())
recur_count = count_fibo_recur(n)
dp_count = count_fibo_dp(n)
print(recur_count, dp_count)
