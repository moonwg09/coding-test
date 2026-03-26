# binary tree traversal(boj 1991)

num_node = int(input())

#트리 생성하기 using dictionary
tree = {} #dict()
for _ in range(num_node):
    data, left, right = input().strip().split()
    tree[data] = [left,right]

def preorder(data):
    if data == '.' : return
    print(data, end = '') # 자기 할 일
    preorder(tree[data][0]) # left subtree
    preorder(tree[data][1]) # right subtree

def inorder(data):
    if data == '.' : return
    inorder(tree[data][0]) # left subtree
    print(data, end = '') # 자기 할 일
    inorder(tree[data][1]) # right subtree

def postorder(data):
    if data == '.' : return
    postorder(tree[data][0]) # left subtree
    postorder(tree[data][1]) # right subtree
    print(data, end = '') # 자기 할 일
    
preorder('A')
print()
inorder('A')
print()
postorder('A')