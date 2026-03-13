import sys
input = sys.stdin.readline

N = int(input())
stack = []
top = -1

for _ in range(N):
    op = input().split() 

    if op[0] == 'push':
        data = int(op[1])
        stack.append(data)
        top += 1

    elif op[0] == 'pop':
        if top >= 0 :
            data = stack.pop()
            top -= 1
            print(data)
        else : 
            print(-1)

    elif op[0] == 'size':
        print(top+1)

    elif op[0] == 'empty':
        if top == -1:
            print(1)
        else :
            print(0)

    elif op[0] == 'top':
        if top >= 0:
            print(stack[top])
        else:
            print(-1)
    
    