from collections import deque

n, k = map(int, input().split())

visited = [0] * 100001

def bfs(start, end):
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        
        if node == end:
            print(visited[node])
            return

        for adj_node in (node - 1, node + 1, node * 2):
            if 0 <= adj_node <= 100000 and visited[adj_node] == 0:
                visited[adj_node] = visited[node] + 1
                queue.append(adj_node)

bfs(n, k)