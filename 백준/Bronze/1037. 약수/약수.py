
count = int(input())



divisor = list(map(int,input().split()))

divisor.sort()

num = divisor[0] * divisor[-1]

print(num)

