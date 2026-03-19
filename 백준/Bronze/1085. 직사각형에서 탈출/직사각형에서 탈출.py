num = list(map(int,input().split()))

x = num[0]
y = num[1]
w = num[2]
h = num[3]

rect = []

rect.append(h-y)
rect.append(w-x)
rect.append(x)
rect.append(y)

len = min(rect)

print(len)