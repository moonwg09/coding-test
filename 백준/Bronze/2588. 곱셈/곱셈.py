
num1 = int(input())
num2 = input()
num3 = list(map(int, num2))
num2 = int(num2)
total = num1 * num2

first = str(num1*num3[-1])
first = list(map(int,first))
print(*first,sep="")

second = str(num1*num3[1])
second = list(map(int,second))
print(*second,sep="")

third = str(num1*num3[0])
third = list(map(int,third))
print(*third,sep="")

print(total)
