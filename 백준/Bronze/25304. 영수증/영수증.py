price = int(input())

count = int(input())

total = 0

for i in range(count):

    a,b = map(int, input().split())

    total += (a * b)

if total == price:
    print("Yes")
else : 
    print("No")