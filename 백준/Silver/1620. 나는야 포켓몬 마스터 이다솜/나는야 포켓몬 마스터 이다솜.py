import sys

input = sys.stdin.readline

n, m = map(int, input().split())

name_id = {}
id_name = {}

for i in range(1, n + 1):
    name = input().strip() 
    name_id[name] = i
    id_name[i] = name


for _ in range(m):
    query = input().strip()
    
  
    if query.isdigit():

        print(id_name[int(query)])
    else:

        print(name_id[query])