
from collections import deque
t = int(input())



for _ in range(t):
    n, m = map(int, input().split())
    num_list = list(map(int,input().split()))
    queue = deque([(p,i) for i,p in enumerate(num_list)])
    count = 0
    while queue:

        max_num = max(d[0] for d in queue)

        current = queue.popleft()

        if current[0] < max_num:
            queue.append(current)
        
        elif current[0] == max_num:
            count += 1
            if current[1] == m:
                print(count)
                break


        


    




