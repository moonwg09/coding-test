from collections import deque
import sys
input = sys.stdin.readline

def bfs(n, num_list):
    if n == 1:
        return 0

    visited = [-1] * n
    queue = deque([0]) 
    visited[0] = 0
    
    while queue:
        curr = queue.popleft()
        
        jump_power = num_list[curr]
        
        for i in range(1, jump_power + 1):
            next_node = curr + i
            
            if next_node < n and visited[next_node] == -1:
                visited[next_node] = visited[curr] + 1
                
                if next_node == n - 1:
                    return visited[next_node]
                
                queue.append(next_node)
                
    return -1

n = int(input())
if n == 0:
    print(-1)
else:
    num_list = list(map(int, input().split()))
    print(bfs(n, num_list))