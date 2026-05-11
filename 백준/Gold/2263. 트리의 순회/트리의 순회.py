import sys

sys.setrecursionlimit(100000)  # 재귀 깊이 제한 증가 (n이 최대 100,000이므로)

# 입력
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# 인오더의 노드 위치를 빠르게 찾기 위해 인덱스 배열 생성
inorder_index = [0] * (n + 1)
for i in range(n):
    inorder_index[inorder[i]] = i


# 프리오더를 구하는 재귀 함수
def preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    # 포스트오더의 마지막 노드가 루트
    root = postorder[post_end]
    print(root, end=" ")  # 프리오더: 루트를 먼저 출력

    # 인오더에서 루트 위치 찾기
    root_idx = inorder_index[root]
    left_size = root_idx - in_start  # 왼쪽 서브트리 크기

    # 왼쪽 서브트리 재귀
    preorder(in_start, root_idx - 1, post_start, post_start + left_size - 1)
    # 오른쪽 서브트리 재귀
    preorder(root_idx + 1, in_end, post_start + left_size, post_end - 1)


# 프리오더 출력
preorder(0, n - 1, 0, n - 1)
print()  # 줄바꿈