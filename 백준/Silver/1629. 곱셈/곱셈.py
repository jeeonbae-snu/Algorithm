def modPow(a, b, c):
    # b == 0인 경우 a^0 = 1 (모듈러 연산에서도 동일)
    if b == 0:
        return 1

    # 먼저 a^(b//2)를 재귀적으로 계산
    temp = modPow(a, b // 2, c)

    # 지수가 짝수이면, (a^(b//2))^2가 정답
    if b % 2 == 0:
        return (temp * temp) % c
    # 홀수이면, (a^(b//2))^2 * a가 정답
    else:
        return (temp * temp * a) % c


# 입력 받기
A, B, C = map(int, input().split())
print(modPow(A, B, C))
