N = int(input())
polygon = [tuple(map(int, input().split())) for _ in range(N)]

s = 0
for i in range(N):
    x1, y1 = polygon[i]
    x2, y2 = polygon[(i + 1) % N]   # 마지막엔 0번으로 돌아감
    s += x1 * y2 - x2 * y1          # xi*yj - xj*yi

area = abs(s) / 2
# 문제에서 소수 첫째 자리까지 출력하라면:
print(f"{area:.1f}")
