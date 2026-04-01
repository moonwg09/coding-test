
import sys
input = sys.stdin.readline

visited_list = []

def dfs(node):
    global count 
    # 방문했다고 표시 => 방문한 노드를 모아놓는 리스트 활용
    visited_list.append(node)
    # 할 일 하기
    count += 1
    # 순회
    for adj_node in sorted(graph[node]):
        if adj_node not in visited_list:
            dfs(adj_node)

num_node = int(input())
num_edge = int(input())
graph = [[] for _ in range(num_node+1)]
for _ in range(num_edge):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
dfs(1)
print(count-1)
