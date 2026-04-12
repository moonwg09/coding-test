
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

stack = []
check = 1

num_list= list(map(int,input().split()))
queue = deque(num_list)

while queue:
    current = queue.popleft()
    
    if current == check:
        check += 1
    else:
        stack.append(current)
    
    while stack and stack[-1] == check:
        stack.pop()
        check += 1

if not stack:
    print("Nice")
else:
    print("Sad")
    



    
