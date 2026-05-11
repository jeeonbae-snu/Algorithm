import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))

# 1) 결과 배열을 -1로 초기화
res = [-1] * N

# 2) “미해결 인덱스”를 저장할 스택
stack = []

# 3) 배열을 한 번 순회
for i, val in enumerate(seq):
    # 3‑1) 스택이 비지 않고, 
    #      스택 최상단 값(seq[stack[-1]])이 현재값(val)보다 작으면
    while stack and seq[stack[-1]] < val:
        idx = stack.pop()     # NGE를 찾은 인덱스
        res[idx] = val        # 그 인덱스의 결과를 채워준다
    # 3‑2) 현재 인덱스 i도 스택에 추가
    stack.append(i)

# 4) 스택에 남은 인덱스들은 모두 “오른쪽에 더 큰 수 없음” → res는 이미 -1
print(*res)
