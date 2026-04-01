import sys
# 재귀 깊이 제한 해제
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 1. 미리 그래프를 정렬해둡니다 (DFS 내부에서 정렬 방지)
for i in range(1, n + 1):
    graph[i].sort()

# 2. 딕셔너리 대신 리스트 사용
visited_order = [0] * (n + 1)
count = 1

def dfs(node):
    global count
    visited_order[node] = count  # 현재 노드에 방문 순서 기록
    
    for adj_node in graph[node]:
        if visited_order[adj_node] == 0:  # 0이면 아직 방문 안 한 것
            count += 1
            dfs(adj_node)

dfs(v)

# 3. 결과 출력 (한 번에 출력하는 것이 더 빠를 수 있음)
sys.stdout.write('\n'.join(map(str, visited_order[1:])) + '\n')