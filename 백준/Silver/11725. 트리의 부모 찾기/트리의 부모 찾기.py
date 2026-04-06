import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

family_tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    family_tree[a].append(b)
    family_tree[b].append(a)

parents_note = [0] * (n + 1)

def find_my_kids(me):
    for friend in family_tree[me]:
        
        if parents_note[friend] == 0:
            
            parents_note[friend] = me
            
            find_my_kids(friend)

parents_note[1] = 1 
find_my_kids(1)

for i in range(2, n + 1):
    print(parents_note[i])