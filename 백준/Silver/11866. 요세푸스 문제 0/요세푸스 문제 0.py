from collections import deque

queue = deque()

n, k = map(int, input().split())

for i in range(n):
    queue.append(i+1)

print("<", end="")
while len(queue) > 1:          
    for _ in range(k-1):
        queue.append(queue.popleft())
    print(queue.popleft(), end=', ')

print(queue[0], end='>')