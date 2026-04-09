
t = int(input())

point_list = []

for _ in range(t):
    point = tuple(map(int,input().split()))
    point_list.append(point)

point_list.sort(key=lambda x: (x[0], x[1]))


for list in point_list:

    print(*list)
