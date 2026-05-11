# 입력: D, P  (2 ≤ D ≤ 8, 0 ≤ P ≤ 30)
D, P = map(int, input().split())
LIMIT = 10 ** D         # D자리까지 허용 ⇒ 값 < LIMIT

cur = {1}               # 0단계(곱셈 0회)에서 도달 가능한 수
for _ in range(P):      # 정확히 P단계까지 확장
    nxt = set()
    for x in cur:
        for m in range(2, 10):   # 곱 2‥9
            y = x * m
            if y < LIMIT:
                nxt.add(y)
    cur = nxt
    if not cur:                  # 살아남은 가지가 없으면 조기 탈락
        print(-1)
        break
else:
    print(max(cur))