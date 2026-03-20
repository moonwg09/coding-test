
num = int(input())
jum = []
for _ in range(num):
    jum.append(list(map(int,input().split()))) 

x = []
y = []
for i in range(num):
    x.append(jum[i][0])
    y.append(jum[i][1])

x.sort()
y.sort()

print((x[-1] - x[0]) * (y[-1] - y[0])) 
