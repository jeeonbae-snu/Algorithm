import sys
import bisect
input = sys.stdin.readline

def count_subsets_mitm(weights, C):
    n = len(weights)
    mid = n // 2
    left, right = weights[:mid], weights[mid:]

    # 왼쪽 절반 모든 부분집합 합
    L = []
    for mask in range(1 << len(left)):
        s = 0
        for i in range(len(left)):
            if mask & (1 << i):
                s += left[i]
        if s <= C:
            L.append(s)

    # 오른쪽 절반 모든 부분집합 합
    R = []
    for mask in range(1 << len(right)):
        s = 0
        for i in range(len(right)):
            if mask & (1 << i):
                s += right[i]
        if s <= C:
            R.append(s)

    R.sort()
    ans = 0
    for x in L:
        # C - x 이하인 R의 원소 개수
        ans += bisect.bisect_right(R, C - x)
    return ans

def main():
    N, C = map(int, input().split())
    weights = list(map(int, input().split()))
    print(count_subsets_mitm(weights, C))

if __name__ == "__main__":
    main()