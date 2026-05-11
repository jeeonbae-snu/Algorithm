def combinations(arr, r):
    if r == 0:
        return [[]]  # 조합에 선택할 원소가 없으면 빈 조합 반환
    if len(arr) < r:
        return []  # 원소의 개수가 부족하면 빈 리스트 반환

    result = []
    # 첫 번째 원소를 포함하는 경우
    for comb in combinations(arr[1:], r - 1):
        result.append([arr[0]] + comb)
    # 첫 번째 원소를 제외하는 경우
    result.extend(combinations(arr[1:], r))

    return result

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
combs = combinations(arr, M)
for c in combs:
    print(*c)