from collections import deque

queue = deque()

n, k = map(int, input().split())

for i in range(n):
    queue.append(i+1)

#k-1 숫자는 popleft() -> append()
print("<", end="")
while len(queue) > 1:          
    for _ in range(k-1):
        queue.append(queue.popleft())
    print(queue.popleft(), end=', ')

# k 숫자는 출력
print(queue[0], end='>')
#print(queue.popleft(),'>')