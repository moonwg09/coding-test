import sys
input = sys.stdin.readline

stack = []
N = int(input())

for i in range(N):
    stack = input().split()
    print(f'Case #{i+1}:', end=' ')
    while stack:
        print(stack.pop(), end=' ')