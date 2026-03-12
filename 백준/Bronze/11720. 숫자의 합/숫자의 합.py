num1 = int(input())
numlist = list(map(int,input())) #split을 쓰면 띄어쓰기 되어있는 걸 나누기때문에 공백이 없이 입력하고 싶으면 split을 빼라
sum = 0

for number in numlist:
    sum += number
print(sum)
