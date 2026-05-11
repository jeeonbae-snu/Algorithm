import sys

input = sys.stdin.readline


def classify(s: str) -> int:
    i, j = 0, len(s) - 1

    # 양쪽에서 안쪽으로 검사
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1

    # 모두 일치 → 회문
    if i >= j:
        return 0

    # 보조 함수: 구간 [l..r]이 회문인지 확인
    def is_pal(l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    # 왼쪽 문자 제거 또는 오른쪽 문자 제거
    if is_pal(i + 1, j) or is_pal(i, j - 1):
        return 1  # 유사회문
    return 2  # 불가능


T = int(input())
for _ in range(T):
    s = input().strip()  # 줄바꿈 제거
    print(classify(s))
