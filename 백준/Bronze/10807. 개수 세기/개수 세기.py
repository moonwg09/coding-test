num = int(input())
count = 0

numlist = list(map(int,input().split()))

find = int(input())

for number in numlist:
    if number == find:
        count += 1
print(count)