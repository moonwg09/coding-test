from collections import deque

queue = deque() # 생성자를 만든다

N = int(input())

#카드를 큐에 집어넣는다
for i in range(N):
    queue.append(i+1)

# 조건에 맞을 떄까지 반복한다 => while
while len(queue) > 1 :
    print(queue.popleft(), end=' ')
    queue.append(queue.popleft())

print(queue[0])