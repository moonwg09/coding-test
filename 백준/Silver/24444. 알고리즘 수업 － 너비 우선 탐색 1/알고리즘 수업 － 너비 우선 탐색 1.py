from collections import deque
import sys
input = sys.stdin.readline

graph = [[] for _ in range(8)]

n , m , start = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# count_list = {i: 0 for i in range(1, n + 1)}
visited_list = {i: 0 for i in range(1, n + 1)}
queue = deque()
count = 1

def bfs(start_node):
    global count
    #시작 노드에 대해서 할 일 처리
    queue.append(start_node)
    visited_list[start_node]= count
    # count_list[start_node] = count

    while queue:
        node = queue.popleft()
        for adj_node in sorted(graph[node]):
            if not visited_list[adj_node]:
                queue.append(adj_node)
                count += 1
                visited_list[adj_node] = count
                # count_list[adj_node] = count
                                                    
bfs(start)
for i in range(1, n + 1):
    print(visited_list[i])
