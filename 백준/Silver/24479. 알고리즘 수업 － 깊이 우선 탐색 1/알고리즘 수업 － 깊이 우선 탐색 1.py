
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m , v = map(int,input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited_list = {i: 0 for i in range(1, n + 1)}
count = 1

def dfs(node):
    global count
    visited_list[node] = count
    # 순회
    for adj_node in sorted(graph[node]):
        if not visited_list[adj_node]:
            count += 1
            dfs(adj_node)

dfs(v)

for i in range(1, n + 1):
    print(visited_list[i])