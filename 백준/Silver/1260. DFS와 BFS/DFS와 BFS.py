from collections import deque
n, m , v = map(int,input().split())

# 그래프 만들기
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited_list = []
queue = deque()

def dfs(node):
    # 방문했다고 표시 => 방문한 노드를 모아놓는 리스트 활용
    visited_list.append(node)
    # 할 일 하기
    print(node, end=" ")
    # 순회
    for adj_node in sorted(graph[node]):
        if adj_node not in visited_list:
            dfs(adj_node)


def bfs(start):
    print(start, end = " ")
    queue.append(start)
    visited_list.append(start)
    while queue:
        node = queue.popleft()
        for adj_node in sorted(graph[node]):
            if adj_node not in visited_list:
                visited_list.append(adj_node)       
                print(adj_node, end=" ")                    
                queue.append(adj_node)              

dfs(v)
print()
visited_list.clear()
bfs(v)