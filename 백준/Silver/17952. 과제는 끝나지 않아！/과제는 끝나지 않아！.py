
import sys
input = sys.stdin.readline

stack = []
total = 0

try:
    N = int(input())
    
    for _ in range(N):
        data = list(map(int, input().split()))
        a = data[0]
        
        if a == 0:
            if stack:
                stack[-1] = stack[-1] - 1
                
        elif a == 1:
            b, c = data[1], data[2]
            stack.append(b)
            stack.append(c-1)
        
        if stack and stack[-1] == 0:    
            stack.pop() # c (카운트 0) 제거
            score = stack.pop() # b (점수) 제거
            total += score

except EOFError:
    pass 

print(total)
