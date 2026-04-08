
from collections import deque
n = int(input())

queue = deque()


flag = False

while True:

    router = int(input())
    if router == 0:
        queue.popleft()
    elif router == -1:
        flag = True
        break
    else:
        if len(queue) != n:
            queue.append(router)
        else:
            continue

if flag:
    if len(queue) == 0:
        print("empty")
    else:
        print(*queue)
else:
    print(1)