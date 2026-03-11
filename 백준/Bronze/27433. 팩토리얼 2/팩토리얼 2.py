num = int(input())
total = 1

for i in range(1, num):
    total += (total * i)

print(total)