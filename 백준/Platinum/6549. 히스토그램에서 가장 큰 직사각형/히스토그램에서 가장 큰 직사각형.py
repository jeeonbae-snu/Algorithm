import sys
input = sys.stdin.readline

while True:
    # 한 줄 전체를 읽어서 정수 리스트로 변환
    data = list(map(int, input().split()))
    # N이 0이면 종료
    if data[0] == 0:
        break

    # 첫 번째가 N, 나머지가 히스토그램 높이들
    N = data[0]
    histograms = data[1:]

    max_area = 0
    stack = []

    for i in range(N):
        idx = i
        # 스택 최상단의 높이가 현재 높이보다 크면 pop하며 면적 계산
        while stack and stack[-1][1] > histograms[i]:
            idx, h = stack.pop()
            area = (i - idx) * h
            max_area = max(max_area, area)
        # pop 후에 갱신된 idx를 사용해야 올바른 범위 측정 가능
        stack.append((idx, histograms[i]))

    # 남아 있는 스택 전부 비우며 면적 계산
    while stack:
        idx, h = stack.pop()
        area = (N - idx) * h
        max_area = max(max_area, area)

    print(max_area)
