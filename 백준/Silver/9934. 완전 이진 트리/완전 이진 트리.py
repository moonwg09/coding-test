import sys
input = sys.stdin.readline

k = int(input())
tree_list = list(map(int, input().split()))
tree = [[] for _ in range(k)]

def inorder(list, depth):

    if not list:
        return
        

    mid = len(list) // 2

    tree[depth].append(list[mid])
    

    inorder(list[:mid], depth + 1)
    inorder(list[mid+1:], depth + 1)
inorder(tree_list, 0)

for level in tree:
    print(*level)