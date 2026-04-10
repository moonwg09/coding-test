
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int,input().split())))


v = [([False]*n) for _ in range(n)]


queue = deque()

def bfs(start, end):

    queue.append((start,end))

    while queue:

        a,b = queue.popleft()
        jump = l[a][b]

        if jump == -1:
            print("HaruHaru")
            return 
            
        for (adj1, adj2) in ((a+jump,b), (a, b+jump)):
            if 0<=adj1<n and 0<=adj2<n:
                if v[adj1][adj2] == False:
                    v[adj1][adj2] = True
                    queue.append((adj1,adj2))
    
    print("Hing")
    return     
        
bfs(0,0)

