# [Silver I] 트리 순회 (BOJ 1991)
# 분류: 트리, 재귀
# 접근: 인접 리스트 기반 그래프 탐색

class Node(object):
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

def preorder(node):
    print(node.data, end='')
    if node.left_node is not None:
        preorder(tree[node.left_node])
    if node.right_node is not None:
        preorder(tree[node.right_node])

def inorder(node):
    if node.left_node is not None:
        inorder(tree[node.left_node])
    print(node.data, end='')
    if node.right_node is not None:
        inorder(tree[node.right_node])

def postorder(node):
    if node.left_node is not None:
        postorder(tree[node.left_node])
    if node.right_node is not None:
        postorder(tree[node.right_node])
    print(node.data, end='')

N = int(input())
tree = {}

for i in range(N):
    data, left_node, right_node = input().split()
    if left_node == ".":
        left_node = None
    if right_node == ".":
        right_node = None
    tree[data] = Node(data, left_node, right_node)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])