import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

num_node, num_edge = map(int, input().split())

visited = [False] * (num_node + 1)
graph = [[] for _ in range(num_node + 1)]

for _ in range(num_edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    visited[node] = True  
    for adj_node in graph[node]:
        if not visited[adj_node]:
            dfs(adj_node)

connector = 0


for i in range(1, num_node + 1):
    if  not visited[i]:  
        dfs(i)
        connector += 1  

print(connector)
