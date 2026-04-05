import sys
input = sys.stdin.readline

stack=[]

k = int(input())

for _ in range(k):

    num = int(input())

    if num == 0:
        stack.pop()
    else:
        stack.append(num)

if stack:
    sum_stack = sum(stack)
else:
    sum_stack = 0

print(sum_stack)
