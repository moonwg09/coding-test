num1, num2 = map(int, input().split())
numlist = list(map(int,input().split()))

for number in numlist:
    if num2 > number:
        print(number,end=" ")